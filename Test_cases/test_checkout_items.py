import pytest
import random
import string
import time
from selenium.webdriver.common.by import By
from Base_page.Login_page import SauceLoginPage
from Base_page.Add_to_cart import AddToCartPage
from Base_page.checkout_items import CheckoutItems
from Utilities.coustom_log import Log_Maker
from Test_data.login_test_data import LoginTestData


@pytest.mark.usefixtures("setup")
class TestCheckoutItems:
    logger = Log_Maker.log_gen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.test_data = LoginTestData()
        self.login_page = SauceLoginPage(self.driver)
        self.cart_page = AddToCartPage(self.driver)
        self.checkout_page = CheckoutItems(self.driver)

    def generate_random_string(self, length=6):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_postal_code(self, length=5):
        return ''.join(random.choices(string.digits, k=length))

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_remove_and_checkout(self):
        username = self.test_data.usernames[0]
        self.logger.info(f"Starting test for user: {username}")
        self.driver.get(self.test_data.page_url)

        self.login_page.enter_username(username)
        self.login_page.enter_password(self.test_data.valid_password)
        self.login_page.click_login()

        assert "Swag Labs" in self.driver.title, "Login failed — title mismatch"
        self.logger.info("Login successful.")

        self.logger.info("Adding all items to the cart.")
        added_items = self.cart_page.add_all_items_to_cart()
        self.logger.info(f"Items added: {added_items}")
        assert added_items, "No items were added to the cart."

        self.logger.info("Navigating to cart page.")
        self.cart_page.go_to_cart()
        self.logger.info("Cart page loaded successfully.")

        self.logger.info("Removing 2 items from the cart.")
        removed_items = self.cart_page.remove_items_from_cart(number_to_remove=2)
        self.logger.info(f"Items removed: {removed_items}")
        assert removed_items, "No items were removed from the cart."

        remaining_items = self.cart_page.get_items_in_cart()
        self.logger.info(f"Remaining items in cart: {remaining_items}")

        for item in removed_items:
            assert item not in remaining_items, f"{item} was not removed from the cart."

        for item in added_items:
            if item not in removed_items:
                assert item in remaining_items, f"{item} is missing from the cart."

        self.logger.info("Proceeding to checkout with random data.")

        # Generate random checkout data
        first_name = self.generate_random_string()
        last_name = self.generate_random_string()
        postal_code = self.generate_random_postal_code()

        self.checkout_page.click_checkout_btn()
        self.checkout_page.enter_firstname(first_name)
        self.checkout_page.enter_lastname(last_name)
        self.checkout_page.enter_postal_code(postal_code)
        self.checkout_page.click_continue_btn()
        self.checkout_page.click_finish_btn()

        confirmation_text = self.driver.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your order!']").text
        assert confirmation_text == "Thank you for your order!", "Checkout failed — Confirmation message not found."

        self.logger.info(f"Checkout completed successfully with: {first_name} {last_name}, {postal_code}")

import pytest
from Base_page.Login_page import SauceLoginPage
from Base_page.Add_to_cart import AddToCartPage
from Utilities.coustom_log import Log_Maker
from Test_data.login_test_data import LoginTestData


@pytest.mark.usefixtures("setup")
class TestAddToCart:
    logger = Log_Maker.log_gen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.test_data = LoginTestData()
        self.login_page = SauceLoginPage(self.driver)
        self.cart_page = AddToCartPage(self.driver)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_and_remove_item_to_cart(self):
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

        self.logger.info("Test completed successfully.")

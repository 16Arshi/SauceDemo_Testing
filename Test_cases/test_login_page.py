import pytest
from selenium.webdriver.common.by import By
from Base_page.Login_page import SauceLoginPage
from Utilities.coustom_log import Log_Maker
from Test_data.login_test_data import LoginTestData


@pytest.mark.usefixtures("setup")
class TestSauceLogin:

    logger = Log_Maker.log_gen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.test_data = LoginTestData()  # Instantiate the data class
        self.driver.get(self.test_data.page_url)
        self.login_page = SauceLoginPage(self.driver)

    @pytest.mark.regression
    def test_valid_login(self):
        for username in self.test_data.usernames:
            self.driver.get(self.test_data.page_url)
            self.logger.info(f"=== Testing valid login for user: {username} ===")
            self.login_page.enter_username(username)
            self.login_page.enter_password(self.test_data.valid_password)
            self.login_page.click_login()

            actual_title = self.driver.title
            expected_title = "Swag Labs"

            if actual_title == expected_title:
                self.logger.info(f"Login successful for user: {username}")
                assert True
            else:
                self.logger.warning(f"Login failed for valid user: {username}")
                assert False

    @pytest.mark.sanity
    def test_invalid_login(self):
        for username in self.test_data.invalid_usernames:
            self.driver.get(self.test_data.page_url)
            self.logger.info(f"=== Testing invalid login for user: {username} ===")
            self.login_page.enter_username(username)
            self.login_page.enter_password(self.test_data.invalid_password)
            self.login_page.click_login()

            error_text = self.login_page.get_error_message()
            expected_text = "Epic sadface: Username and password do not match any user in this service"

            if expected_text in error_text:
                self.logger.info(f"Proper error shown for invalid user: {username}")
                assert True
            else:
                self.logger.warning(f"Incorrect or no error for invalid user: {username}")
                assert False

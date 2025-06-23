from selenium.webdriver.common.by import By

class SauceLoginPage:
    user_name_id = "user-name"
    password_id = "password"
    login_id = "login-button"
    error_msg_xpath = "//h3[@data-test='error']"


    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        user_input = self.driver.find_element(By.ID, self.user_name_id)
        user_input.clear()
        user_input.send_keys(username)

    def enter_password(self, password):
        pass_input = self.driver.find_element(By.ID, self.password_id)
        pass_input.clear()
        pass_input.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_id).click()

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, self.error_msg_xpath).text

    def title(self):
        self.driver.find_element(By.CSS_SELECTOR, value=".title")

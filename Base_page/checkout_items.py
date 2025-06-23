import pytest
from selenium.webdriver.common.by import By


class CheckoutItems:
    checkout_btn_id="checkout"
    first_name_id="first-name"
    last_name_id="last-name"
    postal_code_id="postal-code"
    continue_btn_id="continue"
    finish_btn_id="finish"
    last_page_xpath="//h2[normalize-space()='Thank you for your order!']"

    def __init__(self,driver):
        self.driver=driver

    def click_checkout_btn(self):
        self.driver.find_element(By.ID,self.checkout_btn_id).click()

    def enter_firstname(self,fname):
        self.driver.find_element(By.ID,self.first_name_id).send_keys(fname)

    def enter_lastname(self,lname):
        self.driver.find_element(By.ID,self.last_name_id).send_keys(lname)

    def enter_postal_code(self,postalcode):
        self.driver.find_element(By.ID,self.postal_code_id).send_keys(postalcode)

    def click_continue_btn(self):
        self.driver.find_element(By.ID, self.continue_btn_id).click()

    def click_finish_btn(self):
        self.driver.find_element(By.ID, self.finish_btn_id).click()


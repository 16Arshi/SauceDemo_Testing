import time
from selenium.webdriver.common.by import By

class AddToCartPage:
    item_container_class = "inventory_item"
    item_name_class = "inventory_item_name"
    add_button_class = "btn_inventory"
    remove_button_class = "btn_secondary"
    cart_icon_id = "shopping_cart_container"

    def __init__(self, driver):
        self.driver = driver

    def add_all_items_to_cart(self):
        item_names = self.driver.find_elements(By.CLASS_NAME, self.item_name_class)
        add_buttons = self.driver.find_elements(By.CLASS_NAME, self.add_button_class)

        added_items = []
        for i in range(len(add_buttons)):
            add_buttons[i].click()
            added_items.append(item_names[i].text)
        return added_items

    def go_to_cart(self):
        self.driver.find_element(By.ID, self.cart_icon_id).click()
        time.sleep(1)  # Small wait to ensure cart page loads

    def remove_items_from_cart(self, number_to_remove=1):
        removed_items = []

        for _ in range(number_to_remove):
            time.sleep(0.5)  # Give DOM a moment to stabilize
            cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")

            if not cart_items:
                break  # No items to remove

            item = cart_items[0]
            item_name = item.find_element(By.CLASS_NAME, self.item_name_class).text
            remove_button = item.find_element(By.TAG_NAME, "button")
            remove_button.click()
            removed_items.append(item_name)

            time.sleep(0.5)  # Allow DOM to reflect change

        return removed_items

    def get_items_in_cart(self):
        items = self.driver.find_elements(By.CLASS_NAME, self.item_name_class)
        return [item.text for item in items]

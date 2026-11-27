from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        return True

    def add_first_item(self):
        self.driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()

    def cart_count(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
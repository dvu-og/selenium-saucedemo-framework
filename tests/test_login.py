import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    assert InventoryPage(driver).is_loaded()

@pytest.mark.parametrize("user, password, message", [
    ("locked_out_user", "secret_sauce", "locked out"),
    ("standard_user", "wrong_pass", "do not match"),
    ("", "", "Username is required"),
])
def test_invalid_login(driver, user, password, message):
    page = LoginPage(driver)
    page.login(user, password)
    assert message in page.get_error()

def test_add_to_cart(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    inv.is_loaded()
    inv.add_first_item()
    assert inv.cart_count() == "1"
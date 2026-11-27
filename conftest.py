import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    d.get("https://www.saucedemo.com")
    yield d
    d.quit()

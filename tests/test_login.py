import time

import pytest

from conftest import base_url, credentials
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.mark.testDemo1
def test_login(driver,base_url,credentials):
    login=LoginPage(driver)
    login.load(base_url)
    login.login(credentials["username"],credentials["password"])
    time.sleep(5)

@pytest.mark.testDemo2
def test_goto_product_details(driver,base_url,credentials):
    login=LoginPage(driver)
    login.load(base_url)
    login.login(credentials["username"],credentials["password"])

    products_page=ProductsPage(driver)
    products_page.open_product('Sauce Labs Backpack')
    assert 'error_url' in driver.current_url, ' ****** URL does not match.'
import allure
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.title("Login with valid credentials")
@pytest.mark.severity(allure.severity_level.CRITICAL)
def test_login1_pass():
    assert 'hello' == 'hello'


@pytest.mark.title('Check username input in login page')
@pytest.mark.severity(allure.severity_level.NORMAL)
def test_login2_fail(driver):
    driver.get('https://www.saucedemo.com/')
    assert driver.find_element(By.ID, 'user-name').is_displayed() == False


@pytest.mark.title("Login with invalid password")
@pytest.mark.severity(allure.severity_level.NORMAL)
def test_login3():
    assert 1 == 1
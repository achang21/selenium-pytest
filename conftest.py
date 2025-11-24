import os
from pathlib import Path

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from dotenv import load_dotenv

from utils.screenshot_util import take_screenshot

load_dotenv()

@pytest.fixture(scope="session")
def driver(request):
    """
      Initialize WebDriver session based on CLI browser option
      """
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options=ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_experimental_option("prefs",{
            "credentials_enable_service":False,
            "profile.password_manager_enabled":False,
            "profile.password_manager_leak_detection":False,
        })
        # # Option1: Use ChromeDriverManager
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        # Option2: Use the downloaded chrome driver
        chrome_driver = Path(os.getcwd(),'drivers/chromedriver')
        driver=webdriver.Chrome(service=ChromeService(chrome_driver),options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        # # Option1: Use FirefoxDriverManager
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        # Option2: Use the downloaded chrome driver
        ff_driver = Path(os.getcwd(),'drivers/geckodriver')
        driver=webdriver.Firefox(service=FirefoxService(ff_driver),options=options)
    else:
        raise Exception(f"[Error] ****** Browser type:{browser} not supported!")

    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture
def credentials():
    return {
        "username":os.getenv("USERNAME"),
        "password":os.getenv("PASSWORD")
    }
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome=yield
#     report=outcome.get_result()
#
#     if report.when=='call' and report.failed:
#         driver=item.funcargs.get('driver')
#         if driver:
#             take_screenshot(driver,f'FAILED_{item.name}')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
        This hook is executed after each test phase (setup/call/teardown)
        and allows attaching custom data to Allure reports.
    """
    # Get the default report (before modification)
    outcome = yield
    report = outcome.get_result()

    # We only care about the "call" phase (when the test body runs)
    if report.when == 'call':
        driver = item.funcargs.get('driver')

        # Add dynamic title if marker exists
        title_marker = item.get_closest_marker('title')
        if title_marker:
            allure.dynamic.title(title_marker.args[0])
        # Add custom severity if marker exists
        severity_marker = item.get_closest_marker('severity')
        if severity_marker:
            allure.dynamic.severity(severity_marker.args[0])

        # Attach extra info if test failed
        if report.failed:
            # 1) Attach error log
            allure.attach(f"Test {item.name} failed.\n\nError:{report.longrepr}",
                          name='Failed Log',
                          attachment_type=allure.attachment_type.TEXT)
            # 2) Attach a screenshot if available (UI or API case)
            # take a screenshot
            screenshot_path=take_screenshot(driver)

            if os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    allure.attach(
                        f.read(),
                        name='screenshot',
                        attachment_type=allure.attachment_type.PNG
                    )
def pytest_addoption(parser):
    parser.addoption('--env',action='store',default='qa',help='Environment: qa/dev/staging/prod')
    parser.addoption('--browser',action='store',default='chrome',help='Browser: chrome/firefox/edge')

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption('--browser')
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.wait = WebDriverWait(driver,timeout=15)
        self.driver=driver

    def open(self,url:str):
        self.driver.get(url)

    def find(self,locator:tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self,locator:tuple):
        el=self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def type(self,locator:tuple,text:str):
        el=self.find(locator)
        el.clear()
        el.send_keys(text)

    def text_of(self,locator:tuple)->str:
        return self.find(locator).text.strip()

    def is_visible(self,locator:tuple)->bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False


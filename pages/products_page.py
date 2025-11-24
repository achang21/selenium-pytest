from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    def open_product(self,product_name:str):
        self.click((By.LINK_TEXT,product_name))
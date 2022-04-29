from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage():

    select_quantitee ='#quantity'
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def changeQuantity(self, quantity):
        quantity_select = Select(self.driver.find_element(By.CSS_SELECTOR, self.select_quantitee))
        quantity_select.select_by_visible_text(quantity)

    def getQuantity(self):
        return Select(self.driver.find_element(By.CSS_SELECTOR, self.select_quantitee)).first_selected_option.text








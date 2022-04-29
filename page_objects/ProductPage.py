from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPage():

    ajout_panier = 'input[name="submit.add-to-cart"]'

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ajout_panier).click()


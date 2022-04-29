from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BooksPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    premier_article_nouveaute = 'div.a-section.octopus-pc-card-content li '

    def selectFirstBookNouveautes(self):
        self.driver.find_element(By.CSS_SELECTOR, self.premier_article_nouveaute).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, self.premier_article_nouveaute)))


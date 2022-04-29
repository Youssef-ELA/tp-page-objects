from page_objects.BooksPage import BooksPage
from page_objects.CartPage import CartPage
from page_objects.ConfirmationPage import ConfirmationPage
from page_objects.HomePage import HomePage
from page_objects.ProductPage import ProductPage
from selenium import webdriver




def test_amazon1():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()

def test_page_object():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    homePage = HomePage(driver)
    homePage.closeCookies()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()
    booksPage = BooksPage(driver)
    booksPage.selectFirstBookNouveautes()
    productPage = ProductPage(driver)
    productPage.addToCart()
    confirmationPage = ConfirmationPage(driver)
    confirmationPage.openCart()
    cartPage = CartPage(driver)
    cartPage.changeQuantity("2")
    assert "2" == cartPage.getQuantity()








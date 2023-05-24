import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#options = webdriver.ChromeOptions()
#options.add_argument('--incognito')
#options.add_argument("start-maximized")
#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument("disable-web-security")
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
#options.add_argument("disable-extensions")

# Se inicializa el controlador de Chrome
#driver = webdriver.Chrome(executable_path=r"C:\Automatizacion\chromedriver.exe")

@pytest.fixture
def browser():
    # Configura el navegador WebDriver
    driver = webdriver.Chrome()  
    driver.implicitly_wait(10)  

    yield driver
    driver.quit()

def test_login_standard(browser):
    browser.get("https://www.saucedemo.com/")

    username_input = browser.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    #username_input.send_keys("problem_user")
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

    inventory_title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )
    assert inventory_title.text.lower() == "products"

    # Agrega un producto al carrito
    #add_to_cart_button = browser.find_element(By.XPATH, "//button[text()='Add to cartt']")
    add_to_cart_button = browser.find_element(By.XPATH, './/div[@class="inventory_list"]/div[2]/div[2]/div[2]/button')
    add_to_cart_button.click()

    time.sleep(3)

def test_add_cart(browser):
    browser.get("https://www.saucedemo.com/")
    username_input = browser.find_element(By.ID, "user-name")
    #username_input.send_keys("standard_user")
    username_input.send_keys("problem_user")
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    # Agrega un producto al carrito
    #add_to_cart_button = browser.find_element(By.XPATH, "//button[text()='Add to cart']")
    add_to_cart_button = browser.find_element(By.XPATH, './/div[@class="inventory_list"]/div[2]/div[2]/div[2]/button')
    add_to_cart_button.click()

    cart_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"

    
# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login

from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_opt = Options()
    #abre chrome como incognito y desactiva popup de
    #contraseña filtrada, que impedia que los test cases se ejecuten bien
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()
    
@pytest.fixture
def login_in_driver(driver):
    login(driver)  # lanza AssertionError si falla (con screenshot)
    WebDriverWait(driver, 5).until(EC.url_contains("inventory"))
    return driver

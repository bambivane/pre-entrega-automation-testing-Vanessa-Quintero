<<<<<<< HEAD
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage



import pathlib
from datetime import datetime
import time

target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.login_completo("standard_user", "secret_sauce")

    print("URL después de login:", driver.current_url)
    driver.save_screenshot("debug_after_login.png")

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield

    report = outcome.get_result()

    if report.when in ("setup","call") and report.failed:
        driver = item.funcargs.get("driver",None)
        
        if driver:
            timestamp_comun= datetime.now().strftime("%Y%m%d_%H%M%S")
            timestamp_unix = int(time.time())
            file_name= target / f"{report.when}_{item.name}_{timestamp_unix}.png"
            driver.save_screenshot(str(file_name))
=======
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
>>>>>>> 28f0f7ce943122549b61967c841cd92eda3f49b8

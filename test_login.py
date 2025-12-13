from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_validation(login_in_driver):
    driver = login_in_driver
    WebDriverWait(driver, 5).until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url, f"URL actual: {driver.current_url}"

# utils.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, user="standard_user", pwd="secret_sauce", timeout=12):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, timeout)

    # Esperar los campos del login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    wait.until(EC.visibility_of_element_located((By.ID, "password")))
    wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    # Completar credenciales (validación de que escribimos lo correcto)
    u = driver.find_element(By.ID, "user-name")
    p = driver.find_element(By.ID, "password")
    u.clear(); u.send_keys(user)
    p.clear(); p.send_keys(pwd)

    # Confirmar que quedó bien tipeado
    typed = u.get_attribute("value")
    if typed != user:
        driver.save_screenshot("login_bad_input.png")
        raise AssertionError(f"El input de usuario NO contiene '{user}' sino '{typed}'. Ver login_bad_input.png")

    # Click login
    driver.find_element(By.ID, "login-button").click()

    # Esperar: o inventario, o mensaje de error del login
    try:
        wait.until(EC.any_of(
            EC.url_contains("inventory"),
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")),
        ))
    except Exception:
        driver.save_screenshot("login_timeout.png")
        raise AssertionError("El login no avanzó (sin redirección ni error). Ver login_timeout.png")

    # Si no redirigió, leemos el error
    if "inventory" not in driver.current_url:
        try:
            err = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        except Exception:
            err = "(no se encontró el contenedor de error)"
        driver.save_screenshot("login_fail.png")
        raise AssertionError(f"Login fallido: {err}. Ver login_fail.png")

    # Defensa final: asegurar que cargan productos
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    return True

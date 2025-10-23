from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login_validation(login_in_driver):
    driver = login_in_driver

    # Esperar que cargue el inventario y existan productos
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    assert driver.title == "Swag Labs", "El título de la página no coincide"

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No hay productos visibles"

    # 👉 Agregar producto específico: Sauce Labs Bike Light
    add_bike_light = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
    )
    add_bike_light.click()

    # Esperar que aparezca el contador del carrito
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    # Verificar que el contador muestra 1
    assert badge.text == "1", f"El contador debería mostrar 1, pero muestra {badge.text}"

    # Verificar que el carrito contiene el producto correcto
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    # Validar que el nombre del producto en el carrito sea “Sauce

import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos

RUTA_JSON = "datos/productos.json"


@pytest.mark.parametrize("nombre_producto", leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver, nombre_producto):
    driver = login_in_driver  # ya viene logueado y en inventory

    inventory_page = InventoryPage(driver)

    inventory_page.agregar_producto_por_nombre(nombre_producto)
    inventory_page.abrir_carrito()

    cart_page = CartPage(driver)
    assert cart_page.obtener_nombre_producto_carrito() == nombre_producto

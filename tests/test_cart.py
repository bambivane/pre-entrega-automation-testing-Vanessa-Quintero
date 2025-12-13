from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_cart(login_in_driver):
    driver = login_in_driver

    inventory_page = InventoryPage(driver)
    inventory_page.agregar_primer_producto()
    inventory_page.abrir_carrito()

    cart_page = CartPage(driver)
    productos_en_carrito = cart_page.obtener_productos_carrito()

    assert len(productos_en_carrito) == 1

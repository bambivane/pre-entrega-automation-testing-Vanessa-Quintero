from pages.inventory_page import InventoryPage

def test_inventory(login_in_driver):
    driver = login_in_driver  # ya viene logueado y en inventory

    inventory_page = InventoryPage(driver)

    # Verificar que hay productos
    assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario esta vacio"

    # Verificar vacio el carrito al inicio
    assert inventory_page.obtener_conteo_carrito() == 0

    # Agregar el primer producto
    inventory_page.agregar_primer_producto()

    # Verificar el contador del carrito
    assert inventory_page.obtener_conteo_carrito() == 1

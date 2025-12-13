import pytest

from utils.datos import leer_csv_login
from pages.login_page import LoginPage
from utils.logger import logger


@pytest.mark.parametrize("usuario,password,debe_funcionar", leer_csv_login("datos/data_login.csv"))
def test_login_validation(driver, usuario, password, debe_funcionar):
    logger.info("Completando con los datos de usuario")

    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.login_completo(usuario, password)

    if debe_funcionar:
        logger.info("Verificando redireccionamiento dentro de la pagina")
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
        logger.info("Test de login exitoso completado")
    else:
        # si NO debe funcionar, deberías seguir en la página de login
        mensaje_error = login_page.obtener_error()
        assert "Epic sadface" in mensaje_error, "El mensaje de error no se esta mostrando"
        logger.info("Test de login fallido completado con exito")

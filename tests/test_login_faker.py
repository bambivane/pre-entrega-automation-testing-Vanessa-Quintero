import pytest
from faker import Faker
from pages.login_page import LoginPage
from utils.logger import logger

fake = Faker()

@pytest.mark.parametrize("usuario,password", [
    (fake.user_name(), fake.password(length=8)),
    (fake.user_name(), fake.password(length=12)),
])
def test_login_faker(driver, usuario, password):
    logger.info("Abriendo login page")
    login_page = LoginPage(driver).abrir_pagina()

    logger.info(f"Intentando login con usuario fake={usuario}")
    login_page.login_completo(usuario, password)

    mensaje_error = login_page.obtener_error()
    assert "Epic sadface" in mensaje_error, "No se mostró el mensaje de error con credenciales fake"

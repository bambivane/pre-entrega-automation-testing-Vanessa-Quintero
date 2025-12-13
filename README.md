# 🧪 Proyecto de Automation Testing – Selenium + Pytest

Este repositorio contiene un proyecto completo de **Automation Testing** desarrollado en **Python**, utilizando **Selenium WebDriver**, **Pytest** y el patrón **Page Object Model (POM)**.

Forma parte de la *pre‑entrega* del curso de Automation Testing (Talento Tech) y cubre **tests funcionales UI**, **tests data‑driven**, **fixtures**, **manejo de errores**, **reportes** y **buenas prácticas de automatización**.

---

## 🚀 Tecnologías utilizadas

* **Python 3.13**
* **Selenium WebDriver**
* **Pytest**
* **Pytest Fixtures**
* **Page Object Model (POM)**
* **Faker** (datos aleatorios)
* **CSV / JSON** (data‑driven testing)
* **Git & GitHub**

---

## 📂 Estructura del proyecto

```
SELENIUM/
│
├── pages/                  # Page Objects
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── __init__.py
│
├── tests/                  # Casos de prueba
│   ├── test_login.py
│   ├── test_login_faker.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_cart_json.py
│   └── test_api_reqres.py
│
├── utils/                  # Utilidades
│   ├── datos.py            # Lectura CSV
│   ├── lector_json.py      # Lectura JSON
│   ├── logger.py           # Logging
│   └── __init__.py
│
├── datos/                  # Data-driven files
│   ├── data_login.csv
│   └── productos.json
│
├── reports/
│   └── screens/            # Screenshots automáticos en fallos
│
├── conftest.py              # Fixtures globales
├── requirements.txt
└── README.md
```

---

## 🔑 Sitio bajo prueba

* **URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)
* Aplicación demo para pruebas de login, inventario y carrito

---

## 🧠 Conceptos aplicados

* Page Object Model (separación de lógica y tests)
* Fixtures reutilizables (`driver`, `login_in_driver`)
* Data‑driven testing con CSV y JSON
* Manejo de esperas explícitas (WebDriverWait)
* Manejo de errores y screenshots automáticos
* Parametrización con `@pytest.mark.parametrize`

---

## 🧪 Casos de prueba implementados

### 🔐 Login

* Login válido
* Login inválido (CSV)
* Login inválido con datos aleatorios (Faker)
* Validación de mensajes de error

### 📦 Inventario

* Verificación de productos visibles
* Carrito vacío al inicio
* Agregado de productos
* Validación del contador del carrito

### 🛒 Carrito

* Agregar primer producto
* Agregar producto por nombre (JSON)
* Validar producto agregado

### 🌐 API (ReqRes)

* Tests GET / POST / DELETE
* Skipped cuando no hay API Key

---

## ⚙️ Instalación y ejecución

### 1️⃣ Crear entorno virtual

```bash
python -m venv .venv
```

### 2️⃣ Activar entorno

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar todos los tests

```bash
pytest -vv -s
```

### 5️⃣ Ejecutar un test específico

```bash
pytest tests/test_login.py -vv -s
```

---

## 📸 Evidencias automáticas

* Cuando un test falla, se guarda un **screenshot automático** en:

```
reports/screens/
```

El nombre del archivo incluye:

* fase (setup/call)
* nombre del test
* timestamp

---

## 🧾 Logging

El proyecto utiliza un **logger personalizado** para:

* Seguimiento de pasos
* Mensajes informativos
* Debug de fallos

---

## 🧑‍💻 Autor

**Vanessa Quintero**
QA Tester / Automation Trainee

GitHub: [https://github.com/bambivane](https://github.com/bambivane)

---

## ✅ Estado del proyecto

✔ Tests UI funcionales
✔ Data‑driven testing
✔ Fixtures y POM
✔ Subido a GitHub

📌 Proyecto listo para evaluación / Entrega final.

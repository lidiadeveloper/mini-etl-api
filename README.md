# 🛠️ Mini ETL + API con FastAPI  
![Tests](https://github.com/lidiadeveloper/mini-etl-api/actions/workflows/tests.yml/badge.svg)

> Proyecto de práctica desarrollado durante mi formación en **Inteligencia Artificial Generativa**.  
> Integra conceptos de Python, manejo de datos (ETL), APIs con FastAPI y pruebas automatizadas con Pytest.

---

## 🚀 Descripción general

Este proyecto simula un pequeño flujo **ETL (Extract, Transform, Load)** y expone los resultados a través de una **API REST**.  
Fue creado como ejercicio para consolidar los fundamentos de desarrollo backend con Python.

**Incluye:**
- 🧩 **ETL simple**: carga y limpieza de datos desde `products.csv`.  
- ⚡ **API con FastAPI**: endpoints REST para consultar y añadir productos.  
- 🧪 **Tests automatizados**: verificación del correcto funcionamiento con `pytest`.  
- 🧰 **CI/CD con GitHub Actions**: ejecución automática de tests en cada commit.  

---

## 📂 Estructura del proyecto
```
primer_proyecto/
├─ app/            → Lógica de la API con FastAPI
│  └─ main.py
├─ src/            → Código ETL (carga de datos)
│  └─ etl.py
├─ data/           → Datos de ejemplo
│  └─ products.csv
├─ tests/          → Pruebas automatizadas
│  └─ test_smoke.py
├─ .github/workflows/tests.yml → Configuración CI
├─ requirements.txt
└─ README.md
```

---

## 🧠 Conceptos aplicados

- Programación estructurada en **Python**
- Validación de datos con **Pydantic**
- Construcción de endpoints con **FastAPI**
- Testing con **Pytest**
- Integración continua con **GitHub Actions**
- Control de versiones con **Git**
- Buenas prácticas de documentación (`README`, `requirements.txt`, estructura limpia)

---

## 🧩 Endpoints principales

| Método | Endpoint | Descripción |
|--------|-----------|--------------|
| `GET` | `/health` | Comprueba el estado de la API |
| `GET` | `/items` | Devuelve todos los productos |
| `GET` | `/items?max_price=20` | Filtra productos con precio ≤ 20 |
| `POST` | `/items` | Añade un nuevo producto |

**Ejemplo JSON:**
```json
{ "id": 4, "name": "Gorra", "price": 9.9 }
```

---

## 🧪 Ejecución local

1. **Crear entorno virtual**
   ```bash
   py -3.13 -m venv .venv
   .\.venv\Scripts\activate   # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar servidor**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Abrir en navegador**
   👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

5. **Ejecutar tests**
   ```bash
   pytest -q
   ```

---

## 💡 Aprendizajes clave

- Cómo crear una **API profesional** con FastAPI.  
- Cómo organizar un proyecto limpio con estructura modular.  
- Cómo validar datos y controlar errores en endpoints.  
- Cómo usar **pytest** y CI/CD para mantener calidad de código.  
- Cómo documentar proyectos técnicos para LinkedIn y portafolio.

---

## 🌱 Próximos pasos

- Integrar **base de datos SQLite** o PostgreSQL.  
- Añadir autenticación básica.  
- Implementar interfaz frontend sencilla (por ejemplo, con Streamlit o React).  
- Desplegar en la nube (Render, Hugging Face o AWS).  

---

## 👩‍💻 Sobre mí

**Lidia García**  
📍 Valencia, España  
🎯 En formación para convertirme en **Ingeniera de IA Generativa**  
💼 LinkedIn: [linkedin.com/in/lidia-garcia-pascual](https://www.linkedin.com/in/lidia-garcia-pascual/)





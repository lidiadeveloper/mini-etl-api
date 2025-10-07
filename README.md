# 🛠️ Mini ETL + API con FastAPI

Este es mi **primer proyecto en Python**, donde combino:
- **ETL simple**: cargar y limpiar un CSV (`products.csv`).
- **API con FastAPI**: exponer los datos y permitir añadir productos.
- **Tests automatizados con pytest**: validar que la API funciona.

---

## 🚀 Cómo ejecutar

1. Crear y activar entorno virtual:
   ```bash
   py -3.13 -m venv .venv
   .\.venv\Scripts\activate   # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Lanzar la API:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Abrir en navegador:
   👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📚 Endpoints principales

- `GET /health` → estado de la API.  
- `GET /items` → lista todos los productos.  
- `GET /items?max_price=20` → lista productos con precio ≤ 20.  
- `POST /items` → añade un producto nuevo.  

**Ejemplo JSON:**
```json
{ "id": 4, "name": "Gorra", "price": 9.9 }
```

---

## ✅ Tests

Ejecutar tests:
```bash
pytest -q
```

### Tests incluidos:
- `test_health`: comprueba que la API está viva.  
- `test_add_item_and_duplicate`: añade un producto y rechaza duplicados.  
- `test_filter_items_by_price`: devuelve solo productos ≤ precio dado.  

---

## 📂 Estructura del proyecto
```
primer_proyecto/
├─ app/            # API con FastAPI
│  └─ main.py
├─ src/            # ETL (carga CSV)
│  └─ etl.py
├─ tests/          # Tests con pytest
│  └─ test_smoke.py
├─ data/           # Datos de ejemplo
│  └─ products.csv
├─ requirements.txt
├─ README.md
└─ .gitignore
```

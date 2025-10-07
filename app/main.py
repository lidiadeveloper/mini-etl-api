from fastapi import FastAPI
from pydantic import BaseModel
from src.etl import load_products

app = FastAPI(title="Mini ETL + API")
DB = load_products("data/products.csv")

class ItemIn(BaseModel):
    id: int
    name: str
    price: float

@app.get("/health")
def health():
    return {"status": "ok"}

from typing import Optional

@app.get("/items")
def list_items(max_price: Optional[float] = None):
    if max_price is not None:
        filtered = [item for item in DB if item["price"] <= max_price]
        return {"count": len(filtered), "items": filtered}
    return {"count": len(DB), "items": DB}


@app.post("/items")
def add_item(item: ItemIn):
    if any(x["id"] == item.id for x in DB):
        return {"error": "id ya existe"}
    DB.append(item.model_dump())  # pydantic v2
    return {"message": "ok", "count": len(DB)}

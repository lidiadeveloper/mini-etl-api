import csv

def load_products(csv_path: str):
    items = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append({
                "id": int(row["id"]),
                "name": row["name"].strip(),
                "price": float(row["price"]),
            })
    return items

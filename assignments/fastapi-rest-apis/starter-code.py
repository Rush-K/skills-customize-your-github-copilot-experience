from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sample FastAPI App")


class Item(BaseModel):
    name: str
    price: float = 0.0
    in_stock: bool = True


items = [
    {"id": 1, "name": "Notebook", "price": 3.5, "in_stock": True},
    {"id": 2, "name": "Pen", "price": 1.2, "in_stock": False},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock,
    }
    items.append(new_item)
    return new_item


# TODO: Add GET /items/{item_id}
# TODO: Add validation or error handling for missing items


import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.post("/api/py/items")
def get_items(items: list[str]):
    if not items:
        return {"error": "Invalid input. Expected a JSON array."}
    random.shuffle(items)
    print(items)
    return items
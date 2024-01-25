# from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class City(BaseModel):
    id: int
    name: str
    timezone: str

db = []

@app.get("/")
def index():
    return {'key': 'value'}


@app.get("/cities")
def cities():
    return db

@app.post("/cities")
def create_city(city: City):
    db.append(city.model_dump())
    return db


@app.delete("/cities")
def delete_city(city_id: int):
    deleted_city = db.pop(city_id-1)
    return (f"{deleted_city['name']} deleted successfully")
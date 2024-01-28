
""" BaseModel is validating the data being put in 
    the Method which is class <something>()
 """
from fastapi import FastAPI
from pydantic import BaseModel 

import requests 

app = FastAPI()


db = []


class City(BaseModel):
    id: int
    name: str
    provice: str
    timezone: str



@app.get("/get-cities")
def get_city():
    result = []
    for city in db:
        r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
        current_time = r.json()['datetime']
        current_utc =  r.json()['utc_offset']
        result.append({'id': city['id'],'name': city['name'], 'timezone': city['timezone'],'UTC':  current_utc,'current_time': current_time})
    return result
    



@app.post("/create-city")
def create_city(city: City):
    db.append(city.model_dump())
    show_city = db[-1]
    return {"City": f"{show_city['name']} successfully added to the list"}



@app.put("/update-city")
def update_city(city_id: int, city_update: City):
    # Merge the data from the existing city with the updated data and update the city in the database
    update_city = {**db[city_id-1], **city_update.model_dump()}
    db[city_id-1] = update_city
    return {"City": f"{update_city['name']} successfully updated"}



@app.delete("/delete-cities")
def delete_city(city_id: int):
    deleted_city = db.pop(city_id-1)
    return (f"{deleted_city['name']} city deleted successfully")

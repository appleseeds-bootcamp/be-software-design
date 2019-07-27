from bottle import run, get, post, delete, put, request
import json
from dal.mysql_db_adapter import MySqlDBAdapter

_db_adapter = MySqlDBAdapter()

@get("/animals")
def get_all_animals():
    animals_list = _db_adapter.get_all_animals()

    return json.dumps(animals_list)

@get("/animals/<animal_id>")
def get_single_aniamls(animal_id):
    pass

@post("/animals")
def create_animals():
    pass

@delete("/animals")
def delete_animal():
    pass

@put("/animals")
def update_animal():
    pass

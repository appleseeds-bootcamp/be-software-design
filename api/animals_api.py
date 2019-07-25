from bottle import run, get, post, delete, put, request
import json


class AnimalsAPI:
    def __init__(self, db_adapter):
        self._db_adapter = db_adapter

    def run(self):
        run(host="localhost", port="7000")

    @get("/animals")
    def get_all_animals(self):
        animals_list = self._db_adapter.get_all_animals()

        return json.dumps(animals_list)

    @get("/animals/<animal_id>")
    def get_single_aniamls(self, animal_id):
        pass

    @post("/animals")
    def create_animals(self):
        pass

    @delete("/animals")
    def delete_animal(self):
        pass

    @put("/animals")
    def update_animal(self):
        pass

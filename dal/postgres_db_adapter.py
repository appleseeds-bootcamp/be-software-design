from .base_database_adapter import BaseDatabaseAdapter
import psycopg2


class PostgresDBAdapter(BaseDatabaseAdapter):
    def __init__(self):
        self._connection = psycopg2.connect()


    def add_animal(self, animal):
        pass

    def get_animal(self, animal_id):
        return super().get_animal(animal_id)

    def get_all_animals(self):
        return super().get_all_animals()

    def update_animal(self, animal_id, animal_to_update):
        return super().update_animal(animal_id, animal_to_update)

    def delete_animal(self, animal_id):
        return super().delete_animal(animal_id)

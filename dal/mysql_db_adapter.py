from .base_database_adapter import BaseDatabaseAdapter
import pymysql


class MySqlDBAdapter(BaseDatabaseAdapter):
    def __init__(self):
        self._connection = pymysql.connect(host="localhost",
                                           user="root",
                                           password="root",
                                           db="animals")
        


    def add_animal(self, animal):
        try:
            with self._connection.cursor() as cursor:
                sql = f"INSERT INTO animals VALUES('{animal.name}','{animal.type}',{animal.age})"

                cursor.execute(sql)
                cursor.commit()
        except Exception as e:
            print(f"Exception occured when trying to add animal {e}")


    def get_animal(self, animal_id):
        return super().get_animal(animal_id)

    def get_all_animals(self):
        return super().get_all_animals()

    def update_animal(self, animal_id, animal_to_update):
        return super().update_animal(animal_id, animal_to_update)

    def delete_animal(self, animal_id):
        return super().delete_animal(animal_id)

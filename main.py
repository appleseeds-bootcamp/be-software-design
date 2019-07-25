from api.animals_api import AnimalsAPI
from dal.mysql_db_adapter import MySqlDBAdapter
from dal.postgres_db_adapter import PostgresDBAdapter

if __name__ == "__main__":
    api = AnimalsAPI(PostgresDBAdapter())

    api.run()


from abc import ABC, abstractmethod

class BaseDatabaseAdapter(ABC):
    # Create
    @abstractmethod
    def add_animal(self, animal):
        pass
    
    # Read
    @abstractmethod
    def get_animal(self, animal_id):
        pass

    @abstractmethod
    def get_all_animals(self):
        pass

    # Update
    @abstractmethod
    def update_animal(self, animal_id, animal_to_update):
        pass

    # Delete
    @abstractmethod
    def delete_animal(self, animal_id):
        pass
    

    
    

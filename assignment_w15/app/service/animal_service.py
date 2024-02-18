
from app.repositories.animal_repo import Animal_repo

class Animal_service:
    def __init__(self):
        self.animal_repo = Animal_repo()

    def get_animals(self):
        animals = self.animal_repo.get_animals()
        return [animal.as_dict() for animal in animals]

    def search_animals(self, species):
        animals = self.animal_repo.search_animals(species)
        return [animal.as_dict() for animal in animals]

    # cara ke-1 tanpa DTO
    # def update_animal(self, id, animal_data):
    #     updated_animal = self.animal_repo.update_animal(id, animal_data)
    #     return updated_animal
    
    def update_animal(self, id, animal_data_dto):
        updated_animal = self.animal_repo.update_animal(id, animal_data_dto)
        return updated_animal.as_dict()
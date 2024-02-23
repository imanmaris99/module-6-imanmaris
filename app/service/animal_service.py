
from app.repositories.animal_repo import Animal_repo
from app.repositories.animal_repo import Enclosure_repo
from app.models.animal import Animal

class Enclosure_service:
    def __init__(self):
        self.enclosure_repo = Enclosure_repo()

    def get_enclosures(self):
        enclosures = self.enclosure_repo.get_enclosures()
        return [enclosure.as_dict() for enclosure in enclosures]
    
class Animal_service:
    def __init__(self):
        self.animal_repo = Animal_repo()

    def get_animals(self):
        animals = self.animal_repo.get_animals()
        return [animal.as_dict() for animal in animals]

    def search_animals(self, species):
        animals = self.animal_repo.search_animals(species)
        return [animal.as_dict() for animal in animals]

    def create_animal(self, animal_data_dto):
        animal = Animal()

        animal.species = animal_data_dto.species
        animal.age = animal_data_dto.age
        animal.gender = animal_data_dto.gender
        animal.special_requirement = animal_data_dto.special_requirement

        created_animal = self.animal_repo.create_animal(animal)
        return created_animal.as_dict()

    # cara ke-1 tanpa DTO
    # def update_animal(self, id, animal_data):
    #     updated_animal = self.animal_repo.update_animal(id, animal_data)
    #     return updated_animal
    
    def update_animal(self, id, animal_data_dto):
        updated_animal = self.animal_repo.update_animal(id, animal_data_dto)
        return updated_animal.as_dict()
    
    def delete_animal(self, id):
        animal = Animal.query.get(id)
        if not animal:
            return "Animal not available"
        
        delete_animal = self.animal_repo.delete_animal(id)
        return delete_animal.as_dict()
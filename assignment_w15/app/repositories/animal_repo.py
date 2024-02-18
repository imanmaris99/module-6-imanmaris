
from app.models.animal import Animal
from app.utils.database import db

class Animal_repo():
    def get_animals(self):
        animals = Animal.query.all()
        return animals
    
    def search_animals(self, species):
        animals = Animal.query.filter(Animal.species.like(f"%{species}%")).all()
        return animals

    # cara ke-1 tanpa DTO-----------------------
    # def update_animal(self, id, animal):
    #     animal_obj = Animal.query.get(id)
    #     animal_obj.species = animal.species
    #     animal_obj.age = animal.age
    #     animal_obj.gender = animal.gender
    #     animal_obj.special_requirement = animal.special_requirement
        
    #     db.session.commit()
    # ------------------------------------------

    def update_animal(self, id, animal):
        animal_obj = Animal.query.get(id)
        animal_obj.species = animal.species
        animal_obj.age = animal.age
        animal_obj.gender = animal.gender
        animal_obj.special_requirement = animal.special_requirement
        
        db.session.commit()
        return animal_obj

from app.models.animal import Animal
from app.models.enclosure import Enclosure
from app.utils.database import db


class Enclosure_repo():
    def get_enclosures(self):
        enclosures = Enclosure.query.all()
        return enclosures
    

class Animal_repo():
    def get_animals(self):
        animals = Animal.query.all()
        return animals
    
    def create_animal(self, animal):
        db.session.add(animal)
        db.session.commit()
        return animal
    
    def update_animal(self, id, animal):
        animal_obj = Animal.query.get(id)
        animal_obj.species = animal.species
        animal_obj.age = animal.age
        animal_obj.gender = animal.gender
        animal_obj.special_requirement = animal.special_requirement
        
        db.session.commit()
        return animal_obj
    
    def delete_animal(self, id):
        animal_obj = Animal.query.get(id)

        db.session.delete(animal_obj)
        db.session.commit()
        return animal_obj
    
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


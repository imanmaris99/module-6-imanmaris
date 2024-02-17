from app.utils.database import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(100), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(100), nullable=True)
    special_requirement = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'species': self.species,
            'age': self.age,
            'gender': self.gender,
            'special_requirement': self.special_requirement
        }
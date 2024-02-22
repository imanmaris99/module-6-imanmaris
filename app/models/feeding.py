
from app.utils.database import db
from app.models.animal import Animal
from app.models.enclosure import Enclosure

class Feeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    food = db.Column(db.String(100), nullable=False)

    animal = db.relationship('Animal', backref=db.backref('feeding_schedules', lazy=True))
    enclosure = db.relationship('Enclosure', backref=db.backref('feeding_schedules', lazy=True))


    def as_dict(self):
        return {
            'id': self.id,
            'animal_id': self.animal_id,
            'enclosure_id': self.enclosure_id,
            'time': self.time,
            'food': self.food
        }


from app.utils.database import db


class Enclosure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'location': self.location
        }
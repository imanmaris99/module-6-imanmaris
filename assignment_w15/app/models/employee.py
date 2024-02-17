from app.utils.database import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=True)
    schedule = db.Column(db.String(100), nullable=True)


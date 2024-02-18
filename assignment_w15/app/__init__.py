from flask import Flask
from app.controller.animal import animal_route
from app.controller.employee import employee_route
import os
from app.utils.database import db, migrate
from app.models import animal

app = Flask(__name__)

DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')

# Perbaikan: Gunakan "SQLALCHEMY_DATABASE_URI" bukan "SQLALCHEMY_DATABASE_URL"
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

db.init_app(app)
migrate.init_app(app, db)

# Perbaikan: Gunakan url_prefix yang benar sesuai kebutuhan Anda
app.register_blueprint(animal_route.animal_blueprint, url_prefix='/animal')
app.register_blueprint(employee_route.employee_blueprint, url_prefix='/employee')

# implementasi versioning api agar lebih ringkas bisa seperti ini, contohnya
# app.register_blueprint(animal_route.animal_blueprint, url_prefix='/v1/animal')

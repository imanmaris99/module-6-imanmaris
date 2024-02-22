import pytest
from app import app, db
import os
from dotenv import load_dotenv
from flask_migrate import upgrade, downgrade

load_dotenv('.env-test')

@pytest.fixture
def test_app():
    app.config['TESTING'] = True

    DATABASE_TYPE = os.getenv('DATABASE_TYPE')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_PORT = os.getenv('DATABASE_PORT')

    # Perbaikan: Gunakan "SQLALCHEMY_DATABASE_URI" bukan "SQLALCHEMY_DATABASE_URL"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    with app.test_client() as client:
        yield client


@pytest.fixture
def migrate_db(text_app):
    with app.app_context():
        upgrade()

    with app.app_context():
        db.create_all()
        yield db
        downgrade()
        db.session.remove()
        db.drop_all
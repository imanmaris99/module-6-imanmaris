import pytest
from app import app

@pytest.fixture
def test_app():
    '''test application setup'''
    app.config['TESTING'] = True
    with app.app_context():
        yield app


# @pytest.fixture
# def test_client(test_app):
#     '''test client setup'''
#     return app.test_client()

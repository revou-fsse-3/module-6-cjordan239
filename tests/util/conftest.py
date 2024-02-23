import pytest
import os
from app import app, db
from dotenv import load_dotenv

load_dotenv(".env-test")
@pytest.fixture
def test_app():
    app .config['TESTING'] = True
    DATABASE_TYPE = os.getenv('DATABASE_TYPE')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    db.init_app(app)
    with app.test_client() as client:
        yield client

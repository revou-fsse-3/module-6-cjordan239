import pytest
import os
from app import app, db


@pytest.fixture
def test_app():
    app .config['TESTING'] = True
    with app.test_client() as client:
        yield client

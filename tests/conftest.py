import pytest
from app import app


@pytest
def test_app():
    app .config['TESTING'] = True

    with app.test_client() as client:
        yield client


from app import app



def test_app():
    app .config['TESTING'] = True

    with app.test_client() as client:
        yield client


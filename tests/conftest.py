import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['LIVESERVER_PORT'] = 5001
    with app.test_client() as client:
        yield client

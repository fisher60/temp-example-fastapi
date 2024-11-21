from pathlib import Path

import pytest
from starlette.testclient import TestClient

from src.main import create_fastapi_app


@pytest.fixture(scope="function", name="test_app")
def get_test_app():
    app = create_fastapi_app(Path(__file__).parent.parent / "test.env")
    yield app


@pytest.fixture(scope="function", name="test_client")
def get_test_client(test_app):
    client = TestClient(test_app, raise_server_exceptions=False)
    yield client


def test_app_root(test_client, test_app):  # Both test_client and test_app are "required" for test
    result = test_client.get("/")
    assert result.json() == {"Hello": "World"}

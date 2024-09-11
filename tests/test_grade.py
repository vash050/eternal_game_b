from fastapi.testclient import TestClient

from main import main_app  # The application with all your endpoints

client = TestClient(main_app)


def test_get_grades():
    response = client.get("/api/v1/general/grade/grades")
    assert response.status_code == 200

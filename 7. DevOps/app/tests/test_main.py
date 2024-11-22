from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_course():
    ## TODO: Check if GET /courses/{course_id} returns status code 200 and that the json response is
    ## correct (as per db) when the course exists
    response = client.get("/courses/CS-E4190")  # Fix the route to API as required
    assert response.status_code == 200
    assert response.json() == {
        "id": "CS-E4190",
        "name": "Cloud software and systems",
        "instructor": "Mario Di francesco",
        "keyword": ["cloud", "container"],
    }
    #assert {"id": "CS-E4190"} == {"id": "CS-1234"}


def test_read_nonexistent_course():
    ## TODO: Check if GET /courses/{course_id} returns status code 404 and that the json response is
    ## {"detail": "Course does not exist"} when the course does not exist
    response = client.get("/courses/CS-1234")  # Fix the route to API as required
    assert response.status_code == 404
    assert response.json() == {"detail": "Course does not exist"}


def test_create_course():
    ## Check if POST /courses/ returns status code 200 and that the json response
    ## contains the correct data if the course does not exist in the db.
    response = client.post(
        "/courses/",
        json={
            "id": "CS-1234",
            "name": "Introduction to Programming",
            "instructor": "John Doe",
            "keyword": ["programming", "basics"],
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "CS-1234",
        "name": "Introduction to Programming",
        "instructor": "John Doe",
        "keyword": ["programming", "basics"],
    }


def test_create_existing_course():
    ## Check if POST /courses/ returns status code 400 and that the json response
    ## is {"detail": "Course already exists"} if the course already exists in the db.
    response = client.post(
        "/courses/",
        json={
            "id": "CS-E4190",
            "name": "Cloud software and systems",
            "instructor": "Mario Di francesco",
            "keyword": ["cloud", "container"],
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Course already exists"}


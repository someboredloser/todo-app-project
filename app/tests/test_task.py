def test_create_task(client, token):
    res = client.post(
        "/tasks",
        json={"title": "Buy milk"},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 201
    assert res.json()["title"] == "Buy milk"


def test_create_task_unauthorized(client):
    res = client.post("/tasks", json={"title": "No auth"})
    assert res.status_code == 401


def test_get_tasks(client, token):
    client.post(
        "/tasks",
        json={"title": "Task 1"},
        headers={"Authorization": f"Bearer {token}"}
    )

    res = client.get(
        "/tasks",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200
    assert isinstance(res.json(), list)
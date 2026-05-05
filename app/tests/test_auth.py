def test_register(client):
    res = client.post("/auth/register", json={
        "email": "a@test.com",
        "password": "123456"
    })

    assert res.status_code == 200
    assert "email" in res.json()


def test_register_duplicate(client):
    client.post("/auth/register", json={
        "email": "dup@test.com",
        "password": "123456"
    })

    res = client.post("/auth/register", json={
        "email": "dup@test.com",
        "password": "123456"
    })

    assert res.status_code in (400, 409)
    
def test_login_success(client):
    client.post("/auth/register", json={
        "email": "login@test.com",
        "password": "123456"
    })

    res = client.post("/auth/login", json={
        "email": "login@test.com",
        "password": "123456"
    })

    assert res.status_code == 200
    assert "access_token" in res.json()


def test_login_wrong_password(client):
    client.post("/auth/register", json={
        "email": "login2@test.com",
        "password": "123456"
    })

    res = client.post("/auth/login", json={
        "email": "login2@test.com",
        "password": "wrong"
    })

    assert res.status_code == 401
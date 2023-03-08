from fastapi import status
from fastapi.testclient import TestClient
from tests.utils.utils import random_email, random_lower_string, random_cpf_pis

users_prefix = "/api/v1/users"

def test_create_user(client: TestClient):
    email = random_email()
    password = random_lower_string()
    random_string = random_lower_string()
    cpf = random_cpf_pis()
    pis = random_cpf_pis()
    data = {
        "user_request": {
            "name": random_string,
            "email": email,
            "cpf": cpf,
            "pis": pis,
            "password": password
        },
        "address_request": {
            "country": random_string,
            "state": random_string,
            "city": random_string,
            "zipcode": random_string,
            "street": random_string,
            "number": random_string
        }
    }
    response = client.post(users_prefix+"/create", json=data)

    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.json()
    assert 'cpf' in response.json()
    assert 'email' in response.json()

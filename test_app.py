import pytest
import requests
from unittest import mock

BASE_URL = "http://127.0.0.1:5000"

@mock.patch("requests.post")
def test_create_user(m_post):
    new_user = {
        "username": "Usuario test 2",
        "password": "senhadetest123"
    }
    m_post.return_value.status_code = 200
    m_post.return_value.json.return_value = {"message": "Usuario cadastrado com sucesso"}

    response = requests.post(url=f"{BASE_URL}/user", json=new_user)

    m_post.assert_called_once_with(url=f"{BASE_URL}/user", json=new_user)

    assert response.status_code == 200
    assert response.json() == {"message": "Usuario cadastrado com sucesso"}

@mock.patch("requests.post")
def test_failed_create_user(m_post):
    new_user = {
        "username": "Usuario test 2",
        "password": ""
    }
    m_post.return_value.status_code = 400
    m_post.return_value.json.return_value = {"message": "Dados invalidos"}

    response = requests.post(url=f"{BASE_URL}/user", json=new_user)

    m_post.assert_called_once_with(url=f"{BASE_URL}/user", json=new_user)

    assert response.status_code == 400
    assert response.json() == {"message": "Dados invalidos"}

@mock.patch("requests.post")
def test_login_success(m_post):
    registered_user = {
        "username": "Usuario test 2",
        "password": "senhadetest123"
    }

    m_post.return_value.status_code = 200
    m_post.return_value.json.return_value = {"message": "Autenticação realizada com sucesso"}

    response = requests.post(url=f"{BASE_URL}/login", json=registered_user)

    assert response.status_code == 200
    assert response.json() == {"message": "Autenticação realizada com sucesso"}


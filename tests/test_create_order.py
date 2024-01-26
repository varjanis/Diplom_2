import requests
import datafile
import auxiliary_functions
import allure
import allure_pytest
import json


class TestCreateOrder:

    @allure.title('Создать заказ с авторизацией')
    def test_create_order_authorized_success(self):

        response = auxiliary_functions.create_user()

        access_token = response.json()["accessToken"]

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6e"]
        }

        response = requests.post(datafile.order_endpoint, headers={'Authorization': access_token}, data=payload)

        order_number = response.json()["order"]["number"]

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()["name"] == "Люминесцентный бургер"

        auxiliary_functions.delete_user(access_token)

    @allure.title('Создать заказ без авторизации')
    def test_create_order_unathorized_success(self):

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }

        response = requests.post(datafile.order_endpoint, data=payload)

        order_number = response.json()["order"]["number"]

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()["name"] == "Флюоресцентный бургер"

    @allure.title('Создать заказ с авторизацией, без ингридиентов')
    def test_create_order_authorized_no_ingredients_fail(self):

        response = auxiliary_functions.create_user()

        access_token = response.json()["accessToken"]

        response = requests.post(datafile.order_endpoint, headers={'Authorization': access_token})

        assert response.status_code == 400
        assert response.json()["success"] == False
        assert response.json()["message"] == "Ingredient ids must be provided"

        auxiliary_functions.delete_user(access_token)

    @allure.title('Создать заказ без авторизации и без ингридиентов')
    def test_create_order_unauthorized_no_ingredients_fail(self):

        response = requests.post(datafile.order_endpoint)

        assert response.status_code == 400
        assert response.json()["success"] == False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Создать заказ с авторизацией и неверными хэшами ингридиентов')
    def test_create_order_authorized_wrong_ingredient_hash_fail(self):

        payload = {
            "ingredients": ["61c0c5a71d1f82001ffgl89s"]
        }

        response = requests.post(datafile.order_endpoint, data=payload)
        assert response.status_code == 500







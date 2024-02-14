import requests
import urls
import allure


class TestCreateOrder:

    @allure.title('Создать заказ с авторизацией')
    def test_create_order_authorized_success(self, setup_user):

        response, token = setup_user

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6e"]
        }

        response = requests.post(urls.order_endpoint, headers={'Authorization': token}, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()["name"] == "Люминесцентный бургер"


    @allure.title('Создать заказ без авторизации')
    def test_create_order_unathorized_success(self):

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }

        response = requests.post(urls.order_endpoint, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()["name"] == "Флюоресцентный бургер"

    @allure.title('Создать заказ с авторизацией, без ингридиентов')
    def test_create_order_authorized_no_ingredients_fail(self, setup_user):

        user_data, token = setup_user

        response = requests.post(urls.order_endpoint, headers={'Authorization': token})

        assert response.status_code == 400
        assert response.json()["success"] == False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Создать заказ без авторизации и без ингридиентов')
    def test_create_order_unauthorized_no_ingredients_fail(self):

        response = requests.post(urls.order_endpoint)

        assert response.status_code == 400
        assert response.json()["success"] == False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Создать заказ с авторизацией и неверными хэшами ингридиентов')
    def test_create_order_authorized_wrong_ingredient_hash_fail(self, setup_user):

        user_data, token = setup_user

        payload = {
            "ingredients": ["61c0c5a71d1f82001ffgl89s"]
        }

        response = requests.post(urls.order_endpoint, data=payload)
        assert response.status_code == 500







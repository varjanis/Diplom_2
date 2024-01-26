import requests
import datafile
import auxiliary_functions
import allure
import allure_pytest
import json

class TestGetUsersOrders:

    @allure.title('Получить список заказов авторизованного пользователя')
    def test_get_users_orders_authorized_success(self):

        response = auxiliary_functions.create_user()

        access_token = response.json()["accessToken"]

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6e"]
        }

        response = requests.post(datafile.order_endpoint, headers={'Authorization': access_token}, data=payload)

        order_number = response.json()["order"]["number"]

        orders_response = requests.get(datafile.order_endpoint, headers={'Authorization': access_token})

        assert orders_response.status_code == 200
        assert orders_response.json()["success"] == True
        assert orders_response.json()["orders"][0]["number"] == order_number

        print(orders_response.json())

        auxiliary_functions.delete_user(access_token)

    @allure.title('Получить список заказов неавторизованного пользователя')
    def test_get_users_orders_unauthorized_fail(self):

        orders_response = requests.get(datafile.order_endpoint)

        assert orders_response.status_code == 401
        assert orders_response.json()["success"] == False
        assert orders_response.json()["message"] == "You should be authorised"

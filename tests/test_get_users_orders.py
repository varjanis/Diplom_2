import requests
import urls
import allure


class TestGetUsersOrders:

    @allure.title('Получить список заказов авторизованного пользователя')
    def test_get_users_orders_authorized_success(self, setup_user):

        user_data, token = setup_user

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6e"]
        }

        response = requests.post(urls.order_endpoint, headers={'Authorization': token}, data=payload)

        order_number = response.json()["order"]["number"]

        orders_response = requests.get(urls.order_endpoint, headers={'Authorization': token})

        assert orders_response.status_code == 200
        assert orders_response.json()["success"] == True
        assert orders_response.json()["orders"][0]["number"] == order_number

        print(orders_response.json())

    @allure.title('Получить список заказов неавторизованного пользователя')
    def test_get_users_orders_unauthorized_fail(self):

        orders_response = requests.get(urls.order_endpoint)

        assert orders_response.status_code == 401
        assert orders_response.json()["success"] == False
        assert orders_response.json()["message"] == "You should be authorised"

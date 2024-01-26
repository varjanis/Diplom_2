import requests
import datafile
import auxiliary_functions
import allure
import allure_pytest
import json


class TestChangeUserData:

    @allure.title('Изменить имя у авторизованного пользователя')
    def test_change_name_authorized_success(self):

        response = auxiliary_functions.create_user()

        access_token = response.json()["accessToken"]

        new_name = auxiliary_functions.generate_random_name()

        data_change_payload = {
            "name": new_name
        }

        data_change_response = requests.patch(datafile.user_endpoint, headers={'Authorization': access_token}, data=data_change_payload)

        assert data_change_response.status_code == 200
        assert data_change_response.json()["success"] == True
        assert data_change_response.json()["user"]["name"] == new_name

        auxiliary_functions.delete_user(access_token)

    @allure.title('Изменить почту у авторизованного пользователя')
    def test_change_email_authorized_success(self):

        response = auxiliary_functions.create_user()

        access_token = response.json()["accessToken"]

        assert response.status_code == 200
        assert response.json()["success"] == True

        new_email = auxiliary_functions.generate_random_email()

        data_change_payload = {
            "email": new_email
        }

        data_change_response = requests.patch(datafile.user_endpoint, headers={'Authorization': access_token},
                                      data=data_change_payload)

        assert data_change_response.status_code == 200
        assert data_change_response.json()["success"] == True
        assert data_change_response.json()["user"]["email"] == new_email

        auxiliary_functions.delete_user(access_token)

    @allure.title('Изменить имя у неавторизованного пользователя')
    def test_change_name_unauthorized_fail(self):

        response = auxiliary_functions.create_user()

        access_token = response.json()["accessToken"]

        new_name = auxiliary_functions.generate_random_name()

        data_change_payload = {
            "email": new_name
        }

        data_change_response = requests.patch(datafile.user_endpoint,
                                              data=data_change_payload)

        assert data_change_response.status_code == 401
        assert data_change_response.json()["success"] == False
        assert data_change_response.json()["message"] == "You should be authorised"

        auxiliary_functions.delete_user(access_token)

    @allure.title('Изменить почту у неавторизованного пользователя')
    def test_change_email_unauthorized_fail(self):
        response = auxiliary_functions.create_user()

        access_token = response.json()["accessToken"]

        new_email = auxiliary_functions.generate_random_email()

        data_change_payload = {
                "email": new_email
            }

        data_change_response = requests.patch(datafile.user_endpoint, data=data_change_payload)

        assert data_change_response.status_code == 401
        assert data_change_response.json()["success"] == False
        assert data_change_response.json()["message"] == "You should be authorised"

        auxiliary_functions.delete_user(access_token)







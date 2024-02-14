import requests
import urls
import auxiliary_functions
import allure


class TestChangeUserData:

    @allure.title('Изменить имя у авторизованного пользователя')
    def test_change_name_authorized_success(self, setup_user):

        user_data, token = setup_user

        new_name = auxiliary_functions.generate_random_name()

        data_change_payload = {
            "name": new_name
        }

        data_change_response = requests.patch(urls.user_endpoint, headers={'Authorization': token}, data=data_change_payload)

        assert data_change_response.status_code == 200
        assert data_change_response.json()["success"] == True
        assert data_change_response.json()["user"]["name"] == new_name


    @allure.title('Изменить почту у авторизованного пользователя')
    def test_change_email_authorized_success(self, setup_user):

        user_data, token = setup_user

        assert user_data.status_code == 200
        assert user_data.json()["success"] == True

        new_email = auxiliary_functions.generate_random_email()

        data_change_payload = {
            "email": new_email
        }

        data_change_response = requests.patch(urls.user_endpoint, headers={'Authorization': token},
                                      data=data_change_payload)

        assert data_change_response.status_code == 200
        assert data_change_response.json()["success"] == True
        assert data_change_response.json()["user"]["email"] == new_email

    @allure.title('Изменить имя у неавторизованного пользователя')
    def test_change_name_unauthorized_fail(self, setup_user):

        new_name = auxiliary_functions.generate_random_name()

        data_change_payload = {
            "email": new_name
        }

        data_change_response = requests.patch(urls.user_endpoint,
                                              data=data_change_payload)

        assert data_change_response.status_code == 401
        assert data_change_response.json()["success"] == False
        assert data_change_response.json()["message"] == "You should be authorised"

    @allure.title('Изменить почту у неавторизованного пользователя')
    def test_change_email_unauthorized_fail(self, setup_user):

        new_email = auxiliary_functions.generate_random_email()

        data_change_payload = {
                "email": new_email
            }

        data_change_response = requests.patch(urls.user_endpoint, data=data_change_payload)

        assert data_change_response.status_code == 401
        assert data_change_response.json()["success"] == False
        assert data_change_response.json()["message"] == "You should be authorised"







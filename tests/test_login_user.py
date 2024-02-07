import requests
import urls
import auxiliary_functions
import allure


class TestUserLogin:

    @allure.title('Авторизация в существующую учетную запись с корректными логином и паролем')
    def test_login_existing_user_success(self):

        email = auxiliary_functions.generate_random_email()
        name = auxiliary_functions.generate_random_name()
        password = auxiliary_functions.generate_random_password()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(urls.register_endpoint, data=payload)

        access_token = response.json()["accessToken"]

        assert response.status_code == 200
        assert response.json()["success"] == True

        login_payload = {
            "email": email,
            "password": password
        }

        login_response = requests.post(urls.login_user_endpoint, data=login_payload)

        assert login_response.status_code == 200
        assert login_response.json()["success"] == True

        auxiliary_functions.delete_user(access_token)

    @allure.title('Нельзя авторизоваться в существующую учетную запись с некорректной почтой')
    def test_login_with_incorrect_login(self):
        email = auxiliary_functions.generate_random_email()
        name = auxiliary_functions.generate_random_name()
        password = auxiliary_functions.generate_random_password()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(urls.register_endpoint, data=payload)

        access_token = response.json()["accessToken"]

        assert response.status_code == 200
        assert response.json()["success"] == True

        login_payload = {
            "email": "somelogin123@mail.ru",
            "password": password
        }

        login_response = requests.post(urls.login_user_endpoint, data=login_payload)

        assert login_response.status_code == 401
        assert login_response.json()["success"] == False
        assert login_response.json()["message"] == "email or password are incorrect"

        auxiliary_functions.delete_user(access_token)

    @allure.title('Нельзя авторизоваться в существующую учетную запись с некорректным паролем')
    def test_login_with_incorrect_password_fail(self):

        email = auxiliary_functions.generate_random_email()
        name = auxiliary_functions.generate_random_name()
        password = auxiliary_functions.generate_random_password()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(urls.register_endpoint, data=payload)

        access_token = response.json()["accessToken"]

        assert response.status_code == 200
        assert response.json()["success"] == True

        login_payload = {
            "email": email,
            "password": "dffnjbhjhkvhjvhj"
        }

        login_response = requests.post(urls.login_user_endpoint, data=login_payload)

        assert login_response.status_code == 401
        assert login_response.json()["success"] == False
        assert login_response.json()["message"] == "email or password are incorrect"

        auxiliary_functions.delete_user(access_token)

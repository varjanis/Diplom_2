import requests
import urls
import auxiliary_functions
import allure


class TestCreateUser:

    @allure.title('Создание нового уникального пользователя c корректными данными')
    def test_create_unique_user_success(self):

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

        auxiliary_functions.delete_user(access_token)

    @allure.title('Нельзя создать нового пользователя, если аккаунт с такими данными уже зарегистрирован')
    def test_create_user_that_already_exists_fail(self):

        email = auxiliary_functions.generate_random_email()
        name = auxiliary_functions.generate_random_name()
        password = auxiliary_functions.generate_random_password()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(urls.register_endpoint, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] == True

        response = requests.post(urls.register_endpoint, data=payload)

        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == "User already exists"

    @allure.title('Нельзя создать нового пользователя, если не заполнена почта')
    def test_create_user_empty_email_fail(self):

        name = auxiliary_functions.generate_random_name()
        password = auxiliary_functions.generate_random_password()

        payload = {
            "email": "",
            "password": password,
            "name": name
        }

        response = requests.post(urls.register_endpoint, data=payload)

        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == "Email, password and name are required fields"


    @allure.title('Нельзя создать нового пользователя, если не заполнен пароль')
    def test_create_user_empty_password_fail(self):

        email = auxiliary_functions.generate_random_email()
        name = auxiliary_functions.generate_random_name()

        payload = {
            "email": email,
            "password": "",
            "name": name
        }

        response = requests.post(urls.register_endpoint, data=payload)

        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title('Нельзя создать нового пользователя, если не заполнено имя')
    def test_create_user_empty_name_fail(self):

        email = auxiliary_functions.generate_random_email()
        password = auxiliary_functions.generate_random_password()

        payload = {
            "email": email,
            "password": password,
            "name": ""
        }

        response = requests.post(urls.register_endpoint, data=payload)

        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == "Email, password and name are required fields"



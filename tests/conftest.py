import pytest
import allure
import auxiliary_functions


@allure.step('Задать тестового пользователя')
@pytest.fixture
def setup_user():

    response = auxiliary_functions.create_user()
    token = response.json()["accessToken"]

    yield response, token

    auxiliary_functions.delete_user(token)

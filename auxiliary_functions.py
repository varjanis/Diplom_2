import random
import string
import requests
import urls
import allure

@allure.step('Сгенерировать случайный пароль')
def generate_random_password():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


@allure.step('Сгенерировать случайное имя')
def generate_random_name():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


@allure.step('Сгенерировать случайную почту')
def generate_random_email():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(7))
    return f'{random_string}@mail.ru'


@allure.step('Создать тестового пользователя')
def create_user():
    email = generate_random_email()
    name = generate_random_name()
    password = generate_random_password()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(urls.register_endpoint, data=payload)

    return response


@allure.step('Удалить тестового пользователя')
def delete_user(token):

    response = requests.delete(urls.user_endpoint, headers={'Authorization': token})
    print('Тестовый пользователь успешно удален')
    return response




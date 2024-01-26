import random
import string
import requests
import datafile
import json


def generate_random_password():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


def generate_random_name():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


def generate_random_email():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(7))
    return f'{random_string}@mail.ru'


def create_user():
    email = generate_random_email()
    name = generate_random_name()
    password = generate_random_password()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(datafile.register_endpoint, data=payload)

    return response


def delete_user(token):

    response = requests.delete(datafile.user_endpoint, headers={'Authorization': token})
    return response




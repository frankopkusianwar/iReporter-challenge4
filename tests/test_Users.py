import unittest
from api.models.db import DatabaseConnection
from flask import request
import json
from tests.base import BaseTest

class TestUsers(BaseTest):
    
    def test_create_user(self):
        user = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"franciscoiv", "email":"jrffgmugabe@gmail.com",
        "password":"23435354646", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data)
        self.assertEqual(message['data'][0]['message'],
                         'user created successfully')
        self.assertEqual(response.status_code,
                         201)

    def test_user_empty_fields(self):
        user = {"firstName":"ofgh", "lastName":"", "":"oki", "username":"francisha", "email":"jrfgmcougabe@gmail.com",
        "password":"", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'fields should be strings')

    def test_for_valid_email(self):
        user = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"francis", "email":"jrfgmugabcom",
        "password":"23435354646", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'invalid email adress')

    def test_check_password_length(self):
        user = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"francis", "email":"jrfgmugabe@gmail.com",
        "password":"234", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'password should be more than 8 characters')

    def test_if_fields_have_string_characters(self):
        user = {"firstName":"ofgh", "lastName":3, "otherNames":"oki", "username":45, "email":"jrffgmugabe@gmail.com",
        "password":"23435354646", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data)
        self.assertEqual(message['message'],
                         'fields should be strings')
        self.assertEqual(response.status_code,
                         200)

    def test_empty_login_fields(self):
        credentials = {"username":"", "password":""}
        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(credentials)
        )
        message = json.loads(response.data)
        self.assertEqual(message['message'],
                         'please enter username and password')
        self.assertEqual(response.status_code,
                         401)

    def test_login_username_not_exist(self):
        credentials = {"username":"xyz", "password":"234"}
        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(credentials)
        )
        message = json.loads(response.data)
        self.assertEqual(message['message'],
                         'username does not exist please register')
        self.assertEqual(response.status_code,
                         401)

    def test_successfull_login(self):
        user_data = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"fran", "email":"jrfgabe@gmail.com",
        "password":"23435354646", "isAdmin":False, "registered":"2019-01-20"}
        credentials = {"username":"fran", "password":"23435354646"}

        self.test_client.post('api/v1/users', content_type = "application/json", data = json.dumps(user_data))
        
        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(credentials)
        )
        self.assertEqual(response.status_code,
                         200)

    def test_invalid_login_password(self):
        
        user_data = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"fran", "email":"jrfgabe@gmail.com",
        "password":"23435354646", "isAdmin":False, "registered":"2019-01-20"}
        credentials = {"username":"fran", "password":"2343535464"}

        self.test_client.post('api/v1/users', content_type = "application/json", data = json.dumps(user_data))

        response = self.test_client.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(credentials)
        )
        message = json.loads(response.data)
        self.assertEqual(message['message'],
                         'invalid password')
        self.assertEqual(response.status_code,
                         401)

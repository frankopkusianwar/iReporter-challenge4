import unittest
from api import create_app
from flask import request
import json
from api.models.db import DatabaseConnection

db = DatabaseConnection()

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("Testing")
        self.test_client = self.app.test_client(self)
        self.db = DatabaseConnection()
        self.db.create_tables()



    def tearDown(self):
        self.test_client = self.app.test_client(self)
        self.db.drop_tables()

    def user_token(self):
        user_data = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"fran", "email":"jrfgabe@gmail.com",
        "password":"23435354646", "isAdmin":False, "registered":"2019-01-20"}
        login_details = {"username":"fran", "password":"23435354646"}
        self.test_client.post('api/v1/users', content_type = "application/json", data = json.dumps(user_data))

        login_response = self.test_client.post('api/v1/login', content_type = "application/json", data = json.dumps(login_details))
        data = json.loads(login_response.data.decode())
        return data['access-token']

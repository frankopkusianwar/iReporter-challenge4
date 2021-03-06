from flask import request, jsonify
from api.utilities import check_email, check_paswd
import uuid
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.db import DatabaseConnection
import jwt

db = DatabaseConnection()


class UserController:
    def create_user(self):
        user_data = request.get_json()
        first_name = user_data.get('firstName')
        last_name = user_data.get('lastName')
        other_names = user_data.get('otherNames')
        username = user_data.get('username')
        email = user_data.get('email')
        password = user_data.get('password')
        registered = datetime.datetime.today()
        is_admin = False

        validate_user = [first_name, last_name,
                         other_names, username, email, password]

        if check_email(email) == "invalid":
            return jsonify({
                "status": 400,
                "message": "invalid email adress"
            }), 400

        if check_paswd(password) == "invalid":
            return jsonify({
                "status": 400,
                "message": "password should be more than 8 characters"
            }), 400
        if db.login(username):
            return jsonify({"message":"username already exists"}), 400
        if db.check_mail(email):
            return jsonify({"message":"email already exists"}), 400

        password_hashed = generate_password_hash(
            user_data.get('password'), method='sha256')
        db.insert_user(first_name, last_name, other_names,
                       username, email, password_hashed, is_admin, registered)

        return jsonify({
            "data": [{
                "status": 201,
                "message": "user created successfully",
            }]
        }), 201

    def login(self):
        auth_data = request.get_json()

        if not db.login(auth_data.get('username')):
            return jsonify({"message":"username does not exist please register"}), 401
        login_user = db.login(auth_data.get('username'))
        if check_password_hash(login_user['password'], auth_data.get('password')):
            access_token = jwt.encode({"userId": login_user['id'], "exp": datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, "franko@pkusianwar")

            user_type = login_user['is_admin']

            return jsonify({'token': access_token.decode('UTF-8'), 'userType': user_type})
        return jsonify({"message": "invalid password"}), 401


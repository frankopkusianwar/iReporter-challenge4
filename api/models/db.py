import os
import psycopg2
import psycopg2.extras


class DatabaseConnection:
    """docstring for DataBaseConnection"""

    def __init__(self):
        #self.db = 'ireporter_db'
        #self.db = 'Ireporter_test_db'
        if os.getenv('ENV') == 'Testing':
            self.db_name='ireporter_test_db'
            self.db_user='postgres'
            self.db_password='security93'
            self.host="127.0.0.1"
        else:
            self.db_name='dfjm31sae6rceq'
            self.db_user='vxxpxavgovowji'
            self.db_password='35ddf4dbab673c413cab9cc521a55cc32ab9d660ce171190c780c8e5398d9c1c'
            self.host="ec2-50-17-193-83.compute-1.amazonaws.com"

        try:
            self.connection = psycopg2.connect(database=self.db_name, user=self.db_user, host=self.host, password=self.db_password, port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            # self.connection = psycopg2.connect(database='ireporter_db', user='postgres', host='localhost', password='security93', port='5432')
            # self.connection.autocommit = True
            # self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            self.create_tables()

        except:
            print('Cannot connect to the database.')

    def create_tables(self):
        create_user_table = """CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,
                        first_name VARCHAR(100), last_name VARCHAR(100), other_names VARCHAR(100),
                        username VARCHAR(100), email VARCHAR(100), password VARCHAR(100), is_admin BOOLEAN, registered DATE);"""
        self.cursor.execute(create_user_table)
        create_incident_table = """CREATE TABLE IF NOT EXISTS incidents(id SERIAL PRIMARY KEY,
                        incident_type VARCHAR(100), location VARCHAR(100), status VARCHAR(100),
                        images VARCHAR(100), videos VARCHAR(100), created_by INT, comment VARCHAR, created_on DATE);"""
        self.cursor.execute(create_incident_table)

    def insert_user(self, first_name, last_name, other_names, username, email, password_hashed, is_admin, registered):
        insert_user = "INSERT INTO users(first_name, last_name, other_names, username, email, password, is_admin, registered) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            first_name, last_name, other_names, username, email, password_hashed, is_admin, registered)
        self.cursor.execute(insert_user)

    def check_mail(self, email):
        query = "SELECT email FROM users WHERE email='{}'".format(email)
        print(query)
        self.cursor.execute(query)
        email = self.cursor.fetchone()
        return email

    def login(self, username):
        query = "SELECT * FROM users WHERE username='{}'".format(username)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def insert_incident(self, incident_type, location, status, images, videos, created_by, comment, created_on):
        insert_incident = "INSERT INTO incidents(incident_type, location, status, images, videos, created_by, comment, created_on) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            incident_type, location, status, images, videos, created_by, comment, created_on)
        self.cursor.execute(insert_incident)

    def get_all_incidents(self):
        query = "SELECT * FROM incidents WHERE incident_type='red-flag'"
        self.cursor.execute(query)
        incidents = self.cursor.fetchall()
        return incidents

    def get_all_interventions(self):
        query = "SELECT * FROM incidents WHERE incident_type='intervention'"
        self.cursor.execute(query)
        incidents = self.cursor.fetchall()
        return incidents

    def get_one_incident(self, incident_Id):
        query_incident = "SELECT * FROM incidents WHERE id='{}' AND incident_type='red-flag'".format(
            incident_Id)
        self.cursor.execute(query_incident)
        incident = self.cursor.fetchone()
        return incident

    def get_one_intervention(self, incident_Id):
        query_incident = "SELECT * FROM incidents WHERE id='{}' AND incident_type='intervention'".format(
            incident_Id)
        self.cursor.execute(query_incident)
        incident = self.cursor.fetchone()
        return incident

    def edit_comment(self, comment, incident_Id):
        edit_comment = "UPDATE incidents SET comment='{}' WHERE id='{}' AND incident_type='red-flag'".format(
            incident_Id, comment)
        self.cursor.execute(edit_comment)

    def edit_intervention_comment(self, comment, incident_Id):
        edit_intervention_comment = "UPDATE incidents SET comment='{}' WHERE id='{}' AND incident_type='intervention'".format(
            incident_Id, comment)
        self.cursor.execute(edit_intervention_comment)

    def edit_location(self, location, incident_Id):
        edit_location = "UPDATE incidents SET location='{}' WHERE id='{}' AND incident_type='intervention'".format(
            incident_Id, location)
        self.cursor.execute(edit_location) 

    def edit_intervention_location(self, location, incident_Id):
        edit_location = "UPDATE incidents SET location='{}' WHERE id='{}' AND incident_type='intervention'".format(
            incident_Id, location)
        self.cursor.execute(edit_location)

    def edit_status(self, status, incident_Id):
        edit_status = "UPDATE incidents SET status='{}' WHERE id='{}'".format(
            incident_Id, status)
        self.cursor.execute(edit_status)

    def edit_intervention_status(self, status, incident_Id):
        edit_intervention_status = "UPDATE incidents SET status='{}' WHERE id='{}'".format(
            incident_Id, status)
        self.cursor.execute(edit_intervention_status)

    def delete_incident(self, incident_Id):
        query = "DELETE FROM incidents WHERE id='{}' AND incident_type='red-flag'".format(incident_Id)
        self.cursor.execute(query)

    def delete_intervention(self, incident_Id):
        query = "DELETE FROM incidents WHERE id='{}' AND incident_type='intervention'".format(incident_Id)
        self.cursor.execute(query)

    def admin(self, cur_user):
        query = "SELECT * FROM users WHERE id='{}' AND is_admin = 'True'".format(cur_user)
        self.cursor.execute(query)
        admin = self.cursor.fetchone()
        return admin

    def drop_tables(self):
        """function that drops the tables"""
        query = "DROP TABLE IF EXISTS users, incidents"
        self.cursor.execute(query)

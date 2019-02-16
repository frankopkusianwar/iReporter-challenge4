from flask import request
import json
from tests.base import BaseTest


class TestEndpoints(BaseTest):

    def test_create_incident(self):
        incident = {"incidentType":"red-flag", "title":"coruption", "description":"coruption", "latitude":"120.00", "longitude":"120.00", "status":"draft", "images":'image-url', "videos":"video-url","createdBy": 2, "comment":"", "created_on":"25-nov-2018"}
        response = self.test_client.post(
            'api/v1/incidents',
            content_type='application/json',
            data=json.dumps(incident),
            headers = {"x-access-token":self.user_token()}
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         'created incident record')

    def test_check_invalid_incident_type(self):
        incident = {"incidentType":"relag", "location":"120.00", "status":"draft", "images":'image-url', "videos":"video-url","createdBy": 2, "comment":"", "created_on":"25-nov-2018"}
        response = self.test_client.post(
            'api/v1/incidents',
            content_type='application/json',
            data=json.dumps(incident),
            headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'please enter incidentType as red-flag or intervention')

    def test_get_all_incidents(self):
        response = self.test_client.get('api/v1/red-flags', headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)

    def test_get_all_incident_records(self):
        response = self.test_client.get('api/v1/incidents', headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)

    #check for getting single red-flag record
    def test_get_single_red_flag(self):
        response = self.test_client.get('api/v1/incidents/{}'.format(1), headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)

    #test whether a comment is added successfully to a red-flag record
    def test_add_comment_to_red_flag(self):
        response = self.test_client.patch('api/v1/incidents/{}/comment'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"comment":"this is a comment"}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         "updated record's comment")

    def test_update_location(self):
        resp = self.test_client.patch('api/v1/incidents/{}/location'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"latitude": "13.00", "longitude": "13.00"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         "updated record's location")

    def test_update_status(self):
        resp = self.test_client.patch('api/v1/incidents/{}/status'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"status":"resolved"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         'status updated successfully')

    def test_delete_red_flag(self):
        response = self.test_client.delete('api/v1/incidents/{}'.format(2),headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         'record has been deleted')

    #check for a red-flag id that does not exist
    def test_check_specific_red_flag_does_not_exist(self):
        response = self.test_client.get('api/v1/incidents/{}'.format(2), headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'record not found')

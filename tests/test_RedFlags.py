from flask import request
import json
from tests.base import BaseTest


class TestEndpoints(BaseTest):

    def test_create_incident(self):
        incident = {"incidentType":"red-flag", "location":"120.00", "status":"draft", "images":'image-url', "videos":"video-url","createdBy": 2, "comment":"", "created_on":"25-nov-2018"}
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

    def test_check_empty_incident_fields(self):
        incident = {"incidentType":"", "location":"", "status":"", "images":"", "videos":"video-url","createdBy": 2, "comment":"", "created_on":"25-nov-2018"}
        response = self.test_client.post(
            'api/v1/incidents',
            content_type='application/json',
            data=json.dumps(incident),
            headers = {"x-access-token":self.user_token()}
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'please fill all fields')

    def test_check_if_fields_are_strings(self):
        incident = {"incidentType":"red-flag", "location":23, "status":45, "images":'image-url', "videos":"video-url","createdBy": 2, "comment":"", "created_on":"25-nov-2018"}
        response = self.test_client.post(
            'api/v1/incidents',
            content_type='application/json',
            data=json.dumps(incident),
            headers = {"x-access-token":self.user_token()}
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'field should be a string')

    def test_get_all_incidents(self):
        response = self.test_client.get('api/v1/red-flags', headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)

    #check for getting single red-flag record
    def test_get_single_red_flag(self):
        response = self.test_client.get('api/v1/red-flags/{}'.format(1), headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)
    #check for getting single intervention record
    def test_get_single_intervention(self):
        response = self.test_client.get('api/v1/interventions/{}'.format(1), headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)

    #test whether a comment is added successfully to a red-flag record
    def test_add_comment_to_red_flag(self):
        response = self.test_client.patch('api/v1/red-flags/{}/comment'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"comment":"this is a comment"}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         "updated red-flag record's comment")

    #test whether a comment is added successfully to an intervention
    def test_add_comment_to_intervention(self):
        response = self.test_client.patch('api/v1/interventions/{}/comment'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"comment":"this is a comment"}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         "updated intervention record's comment")

    def test_update_location(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/location'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"location": "13.00"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         "updated red-flag record's location")

    def test_update_intervention_location(self):
        resp = self.test_client.patch('api/v1/interventions/{}/location'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"location": "13.00"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         "updated red-flag record's location")

    def test_update_status(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/status'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"status":"resolved"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         'only admin can change status')

    def test_update_intervention_status(self):
        resp = self.test_client.patch('api/v1/interventions/{}/status'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"status":"resolved"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         'only admin can change status')

    def test_delete_red_flag(self):
        response = self.test_client.delete('api/v1/red-flags/{}'.format(2),headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         'red-flag record has been deleted')

    def test_delete_intervention(self):
        response = self.test_client.delete('api/v1/interventions/{}'.format(2),headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         'intervention record has been deleted')

    #check for a red-flag id that does not exist
    def test_check_specific_red_flag_does_not_exist(self):
        response = self.test_client.get('api/v1/red-flags/{}'.format(2), headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'requested red-flag-id not found')

    #check for an intervention id that does not exist
    def test_check_specific_intervention_does_not_exist(self):
        response = self.test_client.get('api/v1/interventions/{}'.format(2), headers = {"x-access-token":self.user_token()})
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'requested intervention-id not found')

    def test_add_empty_comment_to_red_flag(self):
        response = self.test_client.patch('api/v1/red-flags/{}/comment'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"comment":""}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "enter comment")

    def test_add_empty_intervention_comment_to_red_flag(self):
        response = self.test_client.patch('api/v1/interventions/{}/comment'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"comment":""}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "enter comment")

    def test_add_empty_location_to_red_flag(self):
        response = self.test_client.patch('api/v1/red-flags/{}/location'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"location":""}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "enter location")

    def test_add_empty_intervention_location_to_red_flag(self):
        response = self.test_client.patch('api/v1/interventions/{}/location'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"location":""}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "enter location")

    def test_add_string_comment_to_red_flag(self):
        response = self.test_client.patch('api/v1/red-flags/{}/comment'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"comment":4}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "enter string")

    def test_add_string_intervention_comment_to_red_flag(self):
        response = self.test_client.patch('api/v1/interventions/{}/comment'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"comment":3}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "enter string")

    def test_add_string_location_to_red_flag(self):
        response = self.test_client.patch('api/v1/red-flags/{}/location'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"location":3}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "enter string")

    def test_add_string_intervention_location_to_red_flag(self):
        response = self.test_client.patch('api/v1/interventions/{}/location'.format(1), content_type='application/json', headers = {"x-access-token":self.user_token()}, data=json.dumps({"location":4}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "enter string")
                         

from flask import request, jsonify
from api.models.db import DatabaseConnection
from api.utilities import check_inc
import uuid
import datetime

db = DatabaseConnection()


class IncidentController:
    def create_incident(self, user_id):
        incident_data = request.get_json()
        incident_type = incident_data.get('incidentType')
        title = incident_data.get('title')
        description = incident_data.get('description')
        latitude = incident_data.get('latitude')
        longitude = incident_data.get('longitude')
        status = "draft"
        created_on = datetime.datetime.today()
        created_by = user_id
        images = incident_data.get('images')
        videos = incident_data.get('videos')
        comment = ""

        validate_fields = [title, description, latitude, longitude, images, videos]

        if incident_type != "red-flag" and incident_type != "intervention":
            return jsonify({"status": 400, "message": "please enter incidentType as red-flag or intervention"}), 400

        db.insert_incident(incident_type, title, description, latitude, longitude, status, images, videos, created_by, comment, created_on)

        return jsonify({
            "data": [{
                "status": 201,
                "message": "created incident record",
            }]
        }), 201

    def get_all_incident_record(self):
        if not db.get_all_incident_records():
            return jsonify({"status": 200, "message": "records not found"})
        return jsonify({
            "status": 200,
            "data": db.get_all_incident_records()
        })

    def get_all_incident(self, user_id):
        if not db.get_all_incidents(user_id):
            return jsonify({"status": 200, "message": "red-flag records not found"})
        return jsonify({
            "status": 200,
            "data": db.get_all_incidents(user_id)
        })

    def get_all_interventions(self, user_id):
        if not db.get_all_interventions(user_id):
            return jsonify({"status": 200, "message": "intervention records not found"})
        return jsonify({
            "status": 200,
            "data": db.get_all_interventions(user_id)
        })

    def get_one_incident(self, particular_id):
        if not db.get_one_incident(particular_id):
            return jsonify({"status": 200, "message": "record not found"})
        return jsonify({
            "status": 200,
            "data": [db.get_one_incident(particular_id)]
        })

    def create_comment(self, comment_id):
        comment_data = request.get_json()
        new_comment = comment_data.get("comment")
        db.edit_comment(comment_id, new_comment)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated record's comment"
            }]
        })

    def update_particular_location(self, location_id):
        location_data = request.get_json()
        new_latitude = location_data.get("latitude")
        new_longitude = location_data.get("longitude")

        db.edit_location(location_id, new_latitude, new_longitude)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated record's location"
            }]
        })

    def change_particular_status(self, current_us, status_id):
        status_data = request.get_json()
        new_status = status_data.get("status")
        db.edit_status(status_id, new_status)
        return jsonify({
            "status": 200,
            "message": "status updated successfully"
        })

    def delete_one_incident(self, delete_id):
        db.delete_incident(delete_id)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "record has been deleted"
            }]
        })

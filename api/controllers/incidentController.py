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
        location = incident_data.get('location')
        status = "draft"
        created_on = datetime.datetime.today()
        created_by = user_id
        images = incident_data.get('images')
        videos = incident_data.get('videos')
        comment = ""

        validate_fields = [location, images, videos]
        for field in validate_fields:
            if type(field) != str:
                return jsonify({"status": 400, "message":"field should be a string"}), 400
        if check_inc(validate_fields) == "invalid":
            return jsonify({"status": 400, "message": "please fill all fields"}), 400
        if incident_type != "red-flag" and incident_type != "intervention":
            return jsonify({"status": 400, "message": "please enter incidentType as red-flag or intervention"}), 400

        db.insert_incident(incident_type, location, status,
                           images, videos, created_by, comment, created_on)

        return jsonify({
            "data": [{
                "status": 201,
                "message": "created incident record",
            }]
        }), 201

    def get_all_incident(self):
        if not db.get_all_incidents():
            return jsonify({"status": 200, "message": "red-flag records not found"})
        return jsonify({
            "status": 200,
            "data": db.get_all_incidents()
        })

    def get_all_interventions(self):
        if not db.get_all_interventions():
            return jsonify({"status": 200, "message": "intervention records not found"})
        return jsonify({
            "status": 200,
            "data": db.get_all_interventions()
        })

    def get_one_incident(self, particular_id):
        if not db.get_one_incident(particular_id):
            return jsonify({"status": 200, "message": "requested red-flag-id not found"})
        return jsonify({
            "status": 200,
            "data": [db.get_one_incident(particular_id)]
        })

    def get_one_intervention(self, particular_id):
        if not db.get_one_intervention(particular_id):
            return jsonify({"status": 200, "message": "requested intervention-id not found"})
        return jsonify({
            "status": 200,
            "data": [db.get_one_intervention(particular_id)]
        })

    def create_comment(self, comment_id):
        comment_data = request.get_json()
        new_comment = comment_data.get("comment")
        if not new_comment:
            return jsonify({"message":"enter comment"})
        if type(new_comment) != str:
            return jsonify({"message":"enter string"})
        db.edit_comment(comment_id, new_comment)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated red-flag record's comment"
            }]
        })

    def create_intervention_comment(self, comment_id):
        comment_data = request.get_json()
        new_comment = comment_data.get("comment")
        if not new_comment:
            return jsonify({"message":"enter comment"})
        if type(new_comment) != str:
            return jsonify({"message":"enter string"})
        db.edit_intervention_comment(comment_id, new_comment)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated intervention record's comment"
            }]
        })

    def update_particular_location(self, location_id):
        location_data = request.get_json()
        new_location = location_data.get("location")
        if not new_location:
            return jsonify({"message":"enter location"})
        if type(new_location) != str:
            return jsonify({"message":"enter string"})
        db.edit_location(location_id, new_location)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated red-flag record's location"
            }]
        })

    def update_intervention_location(self, location_id):
        location_data = request.get_json()
        new_location = location_data.get("location")
        if not new_location:
            return jsonify({"message":"enter location"})
        if type(new_location) != str:
            return jsonify({"message":"enter string"})
        db.edit_intervention_location(location_id, new_location)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated red-flag record's location"
            }]
        })

    def change_particular_status(self, current_us, status_id):
        if db.admin(current_us):
            status_data = request.get_json()
            new_status = status_data.get("status")
            if not new_status:
                return jsonify({"message":"enter status"})
            if type(new_status) != str:
                return jsonify({"message":"enter string"})
            db.edit_status(status_id, new_status)
            return jsonify({
                "status": 200,
                "message": "status updated successfully"
            })
        else:
            return jsonify({"message":"only admin can change status"})

    def change_intervention_status(self, current_us, status_id):
        if db.admin(current_us):
            status_data = request.get_json()
            new_status = status_data.get("status")
            if not new_status:
                return jsonify({"message":"enter status"})
            if type(new_status) != str:
                return jsonify({"message":"enter string"})
            db.edit_intervention_status(status_id, new_status)
            return jsonify({
                "status": 200,
                "message": "status updated successfully"
            })
        else:
            return jsonify({"message":"only admin can change status"})

    def delete_one_incident(self, delete_id):
        db.delete_incident(delete_id)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "red-flag record has been deleted"
            }]
        })

    def delete_one_intervention(self, delete_id):
        db.delete_intervention(delete_id)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "intervention record has been deleted"
            }]
        })

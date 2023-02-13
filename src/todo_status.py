import json

from flask import request, Response
from flask_restful import Resource

from json_validator import validateJson
from models.models import TODO
from src import db


class TodoStatus(Resource):
    def put(self, todo_id):
        request_json = validateJson(request, "todo_status.json")

        if not isinstance(request_json, dict):
            return Response(
                status=400,
                response=json.dumps(request_json),
                content_type="application/json"
            )

        item = TODO.query.filter_by(id=todo_id).first()

        if item:
            todo_status = request_json["todo_status"]
            item.status = todo_status
            db.session.commit()

            message = "The todo with id: " + str(item.id) + ", status updated to'" + str(item.status) + "'"

            return Response(
                status=200,
                response=json.dumps(message),
                content_type="application/json"
            )

        return Response(
            status=403,
            response=json.dumps("Todo Item not found with the given ID"),
            content_type="application/json"
        )

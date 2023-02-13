import json

from flask import Response, request
from flask_restful import Resource

from json_validator import validateJson
from log import log
from models.models import TODO
from src import db


class TodoCreate(Resource):
    def post(self):
        request_json = validateJson(request, "todo_item.json")

        # Checking whether the request_json is an instance of dict data type or not
        if not isinstance(request_json, dict):
            return Response(
                status=400,
                response=json.dumps(request_json),
                content_type="application/json"
            )

        # Adding the call details to the database
        item = TODO(todo_item=request_json["todo_item"])
        db.session.add(item)
        db.session.commit()

        data = ("TODO Item Saved:" + request_json["todo_item"] + " with todo_id: " + str(item.id))
        log.info(data)

        return Response(
            status=200,
            response=json.dumps(data),
            content_type="application/json"
        )

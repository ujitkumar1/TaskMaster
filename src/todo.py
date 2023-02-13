import json

from flask import request, Response
from flask_restful import Resource
from models.models import TODO

class Todo(Resource):
    def get(self,todo_id):
        item = TODO.query.filter_by(id = todo_id).first()

        if item:
            message = "The todo with id: " + str(todo_id) + ", is '" + item.todo_item + "'"
            if item.status == 0:
                message += " and it's incomplete"
            else:
                message += " and it's completed"
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
import json

from flask import request, Response
from flask_restful import Resource

from src.json_validator import validateJson
from src.logger import log
from src.models.models import TODO
from src import db


class TodoStatus(Resource):
    def put(self, todo_id):
        """
            This method updates the status of a single to-do item based on its id and returns a JSON response
            or an error message if the item is not found.
            Args:
                todo_id (int): The id of the to-do item to update the status for.
            Returns:
                Response: A Successful Flask response object if the status was updated successfully,
                else an error message.
        """
        # Validating the JSON Request with todo_status.json
        request_json = validateJson(request, "todo_status.json")

        if not isinstance(request_json, dict):
            log.error(str(request_json))
            return Response(
                status=400,
                response=json.dumps(request_json),
                content_type="application/json"
            )

        # Checking if todo_id is in correct format or not
        if not isinstance(todo_id, int):
            log.error("Todo Id not in correct format")
            return Response(
                status=400,
                response=json.dumps("Todo Id not in correct format"),
                content_type="application/json"
            )

        # Fetching the todo from the database
        item = TODO.query.filter_by(id=todo_id).first()

        if item:
            # Updating the status of the todo
            todo_status = request_json["todo_status"]
            item.status = todo_status
            db.session.commit()

            message = "The todo with id: " + str(item.id) + ", status updated to'" + str(item.status) + "'"
            log.info(message)
            return Response(
                status=200,
                response=json.dumps(message),
                content_type="application/json"
            )

        log.info("Todo Item not found with the given ID")
        return Response(
            status=403,
            response=json.dumps("Todo Item not found with the given ID"),
            content_type="application/json"
        )

import json

from flask import request, Response
from flask_restful import Resource

from json_validator import validateJson
from models.models import TODO
from src import db
from logger import log

class Todo(Resource):
    def get(self, todo_id):
        """
            This method retrieves a single to-do item based on its id and returns a JSON response with the to-do item
            or an error message if the item is not found.
            Args:
                todo_id (int): The id of the to-do item to retrieve.
            Returns:
                Response: A Flask response object with a JSON representation of the to-do item or an error message.
        """

        if not isinstance(todo_id, int):
            error_msg = "Todo Id not in correct format"
            log.error(error_msg)
            return Response(
                status=400,
                response=json.dumps(error_msg),
                content_type="application/json"
            )

        item = TODO.query.filter_by(id=todo_id).first()

        if item:
            message = "The todo with id: " + str(todo_id) + ", is '" + item.todo_item + "'"
            if item.status == 0:
                message += " and it's incomplete"
            else:
                message += " and it's completed"
            log.info(message)
            return Response(
                status=200,
                response=json.dumps(message),
                content_type="application/json"
            )

        log.error("Todo Item not found with the given ID")
        return Response(
            status=403,
            response=json.dumps("Todo Item not found with the given ID"),
            content_type="application/json"
        )

    def delete(self, todo_id):
        """
            This method deletes a single to-do item based on its id and returns a JSON response
            or an error message if the item is not found.
            Args:
                todo_id (int): The id of the to-do item to delete.
            Returns:
                Response: A Successful Flask response object if todo deleted successfully else an error message.
        """

        if not isinstance(todo_id, int):
            log.error("Todo Id not in correct format")
            return Response(
                status=400,
                response=json.dumps("Todo Id not in correct format"),
                content_type="application/json"
            )

        item = TODO.query.filter_by(id=todo_id).first()

        if item:
            db.session.delete(item)
            db.session.commit()

            message = "The todo with id: " + str(todo_id) + ", is '" + item.todo_item + "' is deleted successfully"
            log.info(message)
            return Response(
                status=200,
                response=json.dumps(message),
                content_type="application/json"
            )

        log.error("Todo Item not found with the given ID")
        return Response(
            status=403,
            response=json.dumps("Todo Item not found with the given ID"),
            content_type="application/json"
        )

    def put(self, todo_id):
        """
            This method updates a single to-do item based on its id and returns a JSON response
            or an error message if the item is not found.
            Args:
                todo_id (int): The id of the to-do item to be updated.
            Returns:
                Response: A Successful Flask response object if todo updated successfully else an error message.
        """
        request_json = validateJson(request, "todo_item.json")

        # Checking whether the request_json is an instance of dict data type or not
        if not isinstance(request_json, dict):
            log.error(str(request_json))
            return Response(
                status=400,
                response=json.dumps(request_json),
                content_type="application/json"
            )

        if not isinstance(todo_id, int):
            log.error("Todo Id not in correct format")
            return Response(
                status=400,
                response=json.dumps("Todo Id not in correct format"),
                content_type="application/json"
            )

        item = TODO.query.filter_by(id=todo_id).first()

        if item:
            todo_item = request_json["todo_item"]
            item.todo_item = todo_item
            db.session.commit()

            message = "The todo with id: " + str(item.id) + ", is updated to'" + item.todo_item + "'"
            log.info(message)
            return Response(
                status=200,
                response=json.dumps(message),
                content_type="application/json"
            )

        log.error("Todo Item not found with the given ID")
        return Response(
            status=403,
            response=json.dumps("Todo Item not found with the given ID"),
            content_type="application/json"
        )

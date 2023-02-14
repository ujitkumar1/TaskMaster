from src import app, api
from src.todo import Todo
from src.todo_add import TodoCreate
from src.todo_status import TodoStatus

"""
Main module to run the Flask RESTful API.

This module defines the RESTful API endpoints for a simple to-do list application.
The API allows users to create, retrieve, update and delete to-do items.

Attributes:
    app (Flask): instance of the Flask application.
    api (Api): instance of the Flask-RESTful Api object.
    db (SQLAlchemy): instance of the SQLAlchemy object used for database management.
"""

# API for creating new to-do items.
api.add_resource(TodoCreate, "/create")

# API for for retrieving, updating and deleting to-do items
api.add_resource(Todo, "/todo/<int:todo_id>")

# API for updating the status of to-do items
api.add_resource(TodoStatus, "/todo/status/<int:todo_id>")

if __name__ == "__main__":
    # running the flask app
    app.run(debug=True)

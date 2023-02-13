from src import app, api, db
from todo import Todo
from todo_add import TodoCreate
from todo_status import TodoStatus

api.add_resource(TodoCreate, "/create")
api.add_resource(Todo, "/todo/<int:todo_id>")
api.add_resource(TodoStatus, "/todo/status/<int:todo_id>")
if __name__ == "__main__":
    db.create_all()
    # running the flask app
    app.run(debug=True)

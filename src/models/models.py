from src import db


class TODO(db.Model):
    """
       This is the Model of TODO table
       Attributes of the tables are:
       id -> id of the todo
       todo_item -> Name/Description of todo
       status -> status of todo(Whether completed or not)
    """
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    todo_item = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)

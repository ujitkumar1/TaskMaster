from src import db


class TODO(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    todo_item = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)

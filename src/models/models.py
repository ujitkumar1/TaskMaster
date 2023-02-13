from src import db


class TODO(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    todo_item = db.Column(db.String, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    # 0 -> Incomplete and 1 -> Completed

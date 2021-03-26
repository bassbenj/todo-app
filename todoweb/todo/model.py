from . import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True, nullable=False)
    password = db.Column(db.String, index=False, unique=False, nullable=False)
    status = db.Column(db.String, index=False, unique=False, nullable=False)

    def __init__(self, username, password, status):
        self.username = username
        self.password = password
        self.status = status


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    user_info_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), index=False, unique=False, nullable=False)
    firstname = db.Column(db.String, index=False, unique=False, nullable=False)
    lastname = db.Column(db.String, index=False, unique=False, nullable=False)
    status = db.Column(db.String, index=False, unique=False, nullable=False)

    def __init__(self, user_id, firstname, lastname, status):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.status = status


class TodoList(db.Model):
    __tablename__ = 'todo_list'
    todo_list_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), index=False, unique=False, nullable=False)
    title = db.Column(db.String, index=False, unique=False, nullable=False)
    description = db.Column(db.String, index=False, unique=False, nullable=True)
    due_date = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    priority = db.Column(db.Integer, index=False, unique=False, nullable=False)
    status = db.Column(db.String, index=False, unique=False, nullable=False)

    def __init__(self, user_id, title, description, due_date, priority, status):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
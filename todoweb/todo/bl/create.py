from todo.model import User, UserInfo, TodoList
from datetime import datetime
from todo import db

class dbcreate():
    def create_ticket(user_id, title, description, due_date = datetime.now(), priority = 3, status = 'New'):
        ticket = TodoList(user_id, title, description, due_date, priority, status)
        print(ticket)
        db.session.add(ticket)
        db.session.commit()

    def create_user(username, password, firstname, lastname):
        try:
            print(username, password, firstname, lastname)
            user = User(username = username, password = password, status = 'active')
            db.session.add(user)
            db.session.commit()

            result = User.query.filter_by(username=username).first()

            user_id = result.user_id
            print(user_id)
            user_info = UserInfo(user_id = int(user_id), firstname = firstname, lastname = lastname, status = 'active')
            db.session.add(user_info)
            db.session.commit()

            return True
        except Exception as e:
            print(e)
            return False
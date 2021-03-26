from todo.model import User, UserInfo, TodoList
from todo import db

class dbupdate():
    def update_ticket(todo_list_id, title, description, due_date, priority, status):
        try:
            result = TodoList.query.filter_by(todo_list_id=todo_list_id).first()
            
            user_id = result.user_id

            result.title = title
            result.description = description
            result.due_date = due_date
            result.priority = priority
            result.status = status

            db.session.commit()

            return user_id

        except Exception as e:
            return False

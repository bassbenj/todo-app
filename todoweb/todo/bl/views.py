from todo.model import User, UserInfo, TodoList

class dbview():
    def login(username, password):
        result = User.query.filter_by(username=username, password=password).first()

        if result:
            return result
        else:
            return False

    def todo_list(user_id):
        result = TodoList.query.filter_by(user_id=user_id).all()
        if result:
            return result
        else:
            return False

    def user_info(user_id):
        result = UserInfo.query.filter_by(user_id=user_id).first()

        return result

    def todo_list_by_id(todo_list_id):
        result = TodoList.query.filter_by(todo_list_id=todo_list_id).first()
        if result:
            return result
        else:
            return False
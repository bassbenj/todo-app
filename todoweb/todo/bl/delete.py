from todo.model import User, UserInfo, TodoList
from todo import db

class dbdelete():
	def delete_ticket(todo_list_id):
		try:
			TodoList.query.filter_by(todo_list_id=todo_list_id).delete()
			db.session.commit()

			return True
		except Exception as e:
			return False

	def delete_user(user_id):
		try:
			User.query.filter_by(user_id=user_id).delete()
			db.session.commit()

			return True

		except Exception as e:
			return False
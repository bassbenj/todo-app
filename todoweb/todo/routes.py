
from flask import render_template, request, redirect, url_for
from todo import app

from todo.bl.views import dbview
from todo.bl.create import dbcreate
from todo.bl.delete import dbdelete
from todo.bl.update import dbupdate


@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = dbview.login(username, password)
        if result:
            return redirect(url_for('home',id = result.user_id))
        elif result == False:
            return render_template('index.html')

    return render_template('index.html')


@app.route("/register", methods = ['POST', 'GET'])
def user_reg():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        create_user = dbcreate.create_user(username, password, firstname, lastname)
        if create_user == True:
            return redirect(url_for('index'))
        else:
            return render_template('register.html')

    return render_template('register.html')


@app.route("/home/<id>", methods = ['POST', 'GET'])
def home(id):
    if request.method == 'POST':
        user_id = request.form['user_id']
        todo_list_id = request.form['todo_list_id']
        if request.form['submit'] == 'Delete':
            dbdelete.delete_ticket(todo_list_id=todo_list_id)
        if request.form['submit'] == 'Update':
            return redirect(url_for('edit_task', id = todo_list_id))
            
    user_id = id
    data = dbview.todo_list(user_id)
    user_info = dbview.user_info(user_id)

    return render_template('home.html', data=data, user_info=user_info)


@app.route("/home/<id>/task", methods = ['POST', 'GET'])
def task(id):
    if request.method == 'POST':
        user_id = request.form['user_id']
        title = request.form['title']
        desc = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        status = request.form['status']


        result = dbcreate.create_ticket(user_id, title, desc, due_date, priority, status)
        if result == False:
            return render_template('task.html', user_id = id)
        else:
            return redirect(url_for('home', id = user_id))

    return render_template('task.html', user_id = id)


@app.route("/home/task/<id>/edit", methods = ['POST', 'GET'])
def edit_task(id):
    if request.method =='POST':
        todo_list_id = request.form['todo_list_id']
        title = request.form['title']
        description =request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        status = request.form['status']

        result = dbupdate.update_ticket(todo_list_id, title, description, due_date, priority, status)

        return redirect(url_for('home', id = result))

    todo_list_id = id
    data = dbview.todo_list_by_id(todo_list_id)
    return render_template('edit-task.html', data = data)

@app.route("/delete/<id>", methods = ['POST', 'GET'])
def delete_user(id):
    user_id = id
    dbdelete.delete_user(user_id)
    return redirect(url_for('index'))
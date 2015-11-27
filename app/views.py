"""
Copyright (c) Shujia Huang
Date: 2015-11-27
"""
from flask import render_template
from flask import request

from app import app
from models import Todo

@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template('index.html', todos = todos)

@app.route('/add', methods = ['POST',])
def add():
    content = request.form.get("content")
    todo = Todo(content = content)
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos = todos)

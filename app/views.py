from flask import render_template

from app import app
from models import Todo

@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template('index.html', todos = todos)

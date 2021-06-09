from flask import Flask, render_template
app = Flask(__name__)

from data import Session, Task
session = Session()

@app.route('/')
def hello():
    tasks = session.query(Task).all()
    return render_template('index.html', tasks=tasks)

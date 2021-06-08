from flask import Flask, request, jsonify, abort
app = Flask(__name__)

from data import Task, Session, SQLAlchemyError
session = Session()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new-vacuum')
def new_vacuum():
    task = Task(description='vacuum floor')
    session.add(task)
    session.commit()
    return 'done'

@app.route('/new-wash-dishes')
def new_wash_dishes():
    task = Task(description='wash dishes')
    session.add(task)
    session.commit()
    return 'done'

@app.route('/tasks/')
def tasks():
    tasks = session.query(Task).all()
    rows = [task.to_dict() for task in tasks]
    return {'tasks': rows}

@app.route('/tasks/<int:id>', methods=['GET','PUT'])
def task(id):
    task = session.query(Task).filter_by(id=id).first()
    if task is None:
        abort(404)
    if request.method == 'PUT':
        task.completed = request.json['completed']
        try:
            session.commit()
        except SQLAlchemyError as err:
            err_msg = err._message()
            print(err_msg)
            session.rollback()
            return jsonify({"error": err_msg}), 400
    return {'task': task.to_dict()}

@app.route('/tasks/', methods=['POST'])
def create_task():
    json = request.json
    task = Task(description=json['description'])
    task.completed = json.get('completed', False)
    session.add(task)
    try:
        session.commit()
    except SQLAlchemyError as err:
        err_msg = err._message()
        print(err_msg)
        session.rollback()
        return jsonify({"error": err_msg}), 400

    return {'task': task.to_dict()}

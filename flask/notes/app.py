from flask import Flask, _app_ctx_stack, jsonify, url_for, render_template, request
from sqlalchemy.orm import scoped_session

from models import Note
from schemas import NoteSchema
from database import SessionLocal, engine

app = Flask(__name__)

app.session = scoped_session(
    SessionLocal,
    scopefunc=_app_ctx_stack.__ident_func__
)

session = app.session

@app.route('/')
def index():
    notes = session.query(Note).all()
    return render_template('index.html', notes=notes)

@app.route('/notes/')
def get_notes():
    notes = session.query(Note).all()
    schema = NoteSchema(many=True)
    return jsonify(notes=schema.dump(notes))

@app.route('/notes/', methods=['POST'])
def create_note():
    schema = NoteSchema()
    note = schema.load(request.json, session=session)
    session.add(note)
    session.commit()
    return jsonify(id=note.id)

@app.route('/notes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def note(id):
    schema = NoteSchema()
    note = session.query(Note).get(id)
    if request.method == 'DELETE':
        session.delete(note)
        session.commit()
        return 'deleted'
    elif request.method == 'PUT':
        note = schema.load(request.json, session=session,
                           instance=note, partial=True)
        session.commit()
        return 'updated'
    else:
        return schema.dump(note)


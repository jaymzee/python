import flask
import sqlalchemy

from models import Note
from schemas import NoteSchema
from database import SessionLocal, engine
from flask import Flask, jsonify, render_template, request, abort
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

session = sqlalchemy.orm.scoped_session(
    SessionLocal,
    scopefunc=flask._app_ctx_stack.__ident_func__
)

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
    try:
        schema = NoteSchema()
        note = schema.load(request.json, session=session)
        session.add(note)
        session.commit()
    except Exception as err:
        abort(403, description=err)
    return schema.dump(note)

@app.route('/notes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def note(id):
    schema = NoteSchema()
    note = session.query(Note).get(id)
    if note is None:
        abort(404)
    if request.method == 'DELETE':
        try:
            session.delete(note)
            session.commit()
        except SQLAlchemyError as err:
            abort(403, description=err)
    elif request.method == 'PUT':
        try:
            note = schema.load(request.json, session=session,
                               instance=note, partial=True)
            session.commit()
        except Exception as err:
            abort(403, description=err)
    return schema.dump(note)

@app.errorhandler(403)
def forbidden(e):
    return jsonify(error=str(e)), 403

@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

from flask import Flask, _app_ctx_stack, jsonify, url_for, render_template
from sqlalchemy.orm import scoped_session

from models import Note
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

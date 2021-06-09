from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fsa.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    print("creating database")
    db.create_all()

@app.route('/add/<string:username>')
def add_user(username):
    user = User(username=username, email=f'{username}@aol.com')
    db.session.add(user)
    db.session.commit()
    return 'done'

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

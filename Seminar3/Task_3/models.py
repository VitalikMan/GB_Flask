from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_user.db'
db = SQLAlchemy(app)


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	password = db.Column(db.String(80), nullable=False)

	def __repr__(self):
		return f'{self.username} {self.email} {self.password}'

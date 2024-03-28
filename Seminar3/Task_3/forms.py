from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = StringField("password", validators=[DataRequired()])
    confirm_password = StringField(
        "confirm_password", validators=[DataRequired(), EqualTo("password")]
    )

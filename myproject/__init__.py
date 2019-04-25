import os

from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.validators import ValidationError

mail = Mail()

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "!@#$%^&*()_+QWERTYUIOPASDFGHJKLZXCVBNM<>POIJUHYGTFRDERTYUIKJHBCFDXSDFGHJ"
app.config["SQLALCHEMY_DATABASE_URI"] = "///sqlite" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "josekangethe2@gmail.com"

db=SQLAlchemy(app)

Migrate(app, db)

mail.__init__(app)

class ContactForm(FlaskForm):
    name = TextField("Name", validators = [DataRequired("The name field cannot be empty")])
    email = TextField("Email", validators = [DataRequired(), Email("please enter a valid email address")])
    subject = TextField("Subject", validators = [DataRequired("The subject field cannot be empty")])
    message = TextAreaField("Message", validators = [DataRequired("The message field cannot be empty")])
    submit = SubmitField("SEND")

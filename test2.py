#!/usr/bin/python3

import threading
import time
import sys

# database.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from CTFd.models import db,Teams
from CTFd import CTFdFlask
from os import system
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ctfd@db/ctfd?charset=utf8mb4"
# sqldb = SQLAlchemy(app)
# chal = sys.argv[1]
app = CTFdFlask(__name__)
# sqldb = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ctfd@db/ctfd?charset=utf8mb4"


db.init_app(app)
app.app_context().push()
db.create_all()

for teamname in ["superdash","ky","embek","woofwoof","lowkeynewbey","Lock3y","Robbin","Lotte","PleaseTryAgain","peterdash","Pirate_the_Carribara"]:
	team = Teams.query.filter_by(name=teamname).first()
	from fyp import generateBinaryFlag
	generateBinaryFlag(team)

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

for teamname in ["MrMeow","SudoP0w3r","Jinjaa","localhost","ok","limcs","limcs1","Ryz3n","Ryzenkap","Siak4p","Siak4p_merah","eyesee","halo","alien30","ohno","syaz0keh","ketamgigit","0069","ZeroSixNine","KDU","IntroS-project","Team123456789","TEAM1234","worm","DonAsk","Dream"]:
	team = Teams.query.filter_by(name=teamname).first()
	passphrase = "password"
	system("docker exec server-skr useradd -m %s -s /bin/bash" % teamname)
	system('''docker exec server-skr bash -c 'echo "%s:%s" | chpasswd' ''' % (teamname,passphrase))
	system("docker exec server-skr cp -rp /chal_template/. /home/%s/" % teamname)
	system('''docker exec server-skr bash -c 'chown %s: /home/%s' ''' % (teamname,teamname))
	system('''docker exec server-skr bash -c 'chmod -w /home/%s' ''' % teamname)
	system("docker exec server-skr cp /etc/passwd /ctfuser")
	system("docker exec server-skr cp /etc/shadow /ctfuser")
	system("docker exec server-skr cp /etc/group /ctfuser")

	from fyp import generateBinaryFlag
	generateBinaryFlag(team)

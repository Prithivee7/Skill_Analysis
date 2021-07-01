from flask import Flask, render_template, request
from sqlalchemy import and_


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres: // aistahvibqghkk: 608e89efec4e45b31fede1054f6750a68b3a28ab056647fd4047fcd445cb461e@ec2-3-231-69-204.compute-1.amazonaws.com: 5432/d4jd5b6mfti1lg'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

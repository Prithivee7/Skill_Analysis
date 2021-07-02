from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os
import csv
import sys
import codecs

db = SQLAlchemy()


class Data(db.Model):
    __tablename__ = "full_data"
    serial = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    skill = db.Column(db.String, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Integer, nullable=False)
    total_count = db.Column(db.Integer, nullable=False)


app = Flask(__name__)

# Tell Flask what SQLAlchemy database to use.
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://mzzmarljuuoopa:a16ef88c2745021b4785d24b02b6331c751ff1c611a3a26694e3a97f7146a04a@ec2-107-21-10-179.compute-1.amazonaws.com:5432/d1vn3evkvfn2k7'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)


def main():
    with app.app_context():
        db.create_all()
        f = open("data_skills_final.csv", encoding='latin-1')
        reader = csv.reader(f)
        for serial, job_name, experience, skill, count, percentage, total_count in reader:
            data = Data(serial=serial, job_name=job_name, experience=experience,
                        skill=skill, count=count, percentage=percentage, total_count=total_count)
            print(serial)
            db.session.add(data)
            db.session.commit()


if __name__ == "__main__":
    main()

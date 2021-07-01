from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

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
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://aistahvibqghkk:608e89efec4e45b31fede1054f6750a68b3a28ab056647fd4047fcd445cb461e@ec2-3-231-69-204.compute-1.amazonaws.com:5432/d4jd5b6mfti1lg'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)


def main():
    with app.app_context():
        db.create_all()
        data = Data(serial=21, job_name="Backend", experience=3, skill="MVC",
                    count=222, percentage=43, total_count=515)
        data = Data(serial=22, job_name="Backend", experience=3, skill="MySQL",
                    count=222, percentage=43, total_count=515)
        data = Data(serial=23, job_name="Backend", experience=3, skill="Design Patterns",
                    count=216, percentage=41, total_count=515)
        data = Data(serial=24, job_name="Backend", experience=3, skill="Jquery",
                    count=207, percentage=40, total_count=515)
        data = Data(serial=25, job_name="Backend", experience=3, skill="Azure",
                    count=195, percentage=37, total_count=515)
        data = Data(serial=26, job_name="Backend", experience=3, skill="Deployment",
                    count=192, percentage=37, total_count=515)
        data = Data(serial=27, job_name="Backend", experience=3, skill="Docker",
                    count=162, percentage=31, total_count=515)
        data = Data(serial=28, job_name="Backend", experience=3, skill="CD",
                    count=153, percentage=29, total_count=515)
        data = Data(serial=29, job_name="Backend", experience=3, skill="Devops",
                    count=147, percentage=28, total_count=515)
        data = Data(serial=30, job_name="Backend", experience=3, skill="J2EE",
                    count=138, percentage=26, total_count=515)
        db.session.add(data)
        db.session.commit()


if __name__ == "__main__":
    main()

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    course = db.Column(db.String(50), nullable=False)
    date_joined = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Student(name='{self.name}', course='{self.course}', date_joined='{self.date_joined}')"

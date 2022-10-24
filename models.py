from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    tea_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tea_name = db.Column(db.String, nullable=False, unique=True)
    tea_members = db.relationship('Member', back_populates="mem_team")

    def __init__(self, name):
        self.tea_name = name


class Member(db.Model):

    mem_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mem_name = db.Column(db.String, nullable=False, unique=True)
    mem_tea_id = db.Column(db.Integer, db.ForeignKey('team.tea_id'))
    mem_team = db.relationship('Team', back_populates="tea_members")


    def __init__(self, name, team):
        self.mem_name = name
        self.mem_team = team

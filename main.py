from flask import Flask
from models import db, Team, Member


def create_app():
    app_flask = Flask(__name__)


    #Datendabnk
    app_flask.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite"
    app_flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app_flask)
    return app_flask

    #Selbstnotiz: In SQL Dann Neue Verbindung anlegen -> SQLite und den Pfad zur Instance suchen (C:\Users\zima0125\PycharmProjects\orm_tutorial\instance) bei mir.

app = create_app()

def befuellen():
    team_1 = Team('Team1')
    team_2 = Team('Team2')
    db.session.add_all([team_1, team_2])

    member_1 = Member('Max', team_1)
    member_2 = Member('Berta', team_2)
    member_3 = Member('Maria', team_1)

    db.session.add_all([member_1, member_2, member_3])

    #Auslesen welcher Member ist in welchem Team
    all_members = Member.query.all()
    for member in all_members:
        print(member.mem_name + " ist in Team " + member.mem_team.tea_name)

    #Durchgehen durch alle Teams wer in welchem Team ist
    all_teams = Team.query.all()
    for team in all_teams:
        print("In Team " + team.tea_name + " sind folgende Members:" )
        for member in team.tea_members:
            print(member.mem_name)

    db.session.commit()

with app.app_context():
    db.drop_all()
    db.create_all()
    befuellen()



@app.route('/')
def index():
    return('<h1>Flask ORM Tutorial </h1>')

app.run(debug=True)
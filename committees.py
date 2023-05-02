from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faculty_committees.db'
db = SQLAlchemy(app)

class Committee(db.Model):
    designation = db.Column(db.String(255))
    committee_code = db.Column(db.String(255), primary_key=True )
    committee_name = db.Column(db.String(255), unique=True, nullable=False)
    committee_type = db.Column(db.String(255))

@app.route('/committees')
def committees():
    committee_list = Committee.query.all()
    return render_template('committees.html', committee_list=committee_list)


db.create_all()


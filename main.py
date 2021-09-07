from flask import Flask, render_template, redirect,url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import create_session
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length
import requests
import datetime as dt
from test import country_code, make_news

API_URL = "https://coronavirus-19-api.herokuapp.com/countries"
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "HalloDunia"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///covidData.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
now = dt.datetime.now()
dated = now.strftime("%d-%m-%Y")
response = requests.get(API_URL)
result = response.json()

class DataCovid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(10), nullable=True)
    country_name = db.Column(db.String(100), nullable=True)

db.create_all()

class FormData(FlaskForm):
    country_name = StringField('Country name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    covid = db.session.query(DataCovid).all()
    return render_template("bocil.html", covid=covid, result=result)

@app.route("/add", methods=['POST', 'GET'])
def add():
    form = FormData()
    if form.validate_on_submit():
        country = form.country_name.data
        new_data = DataCovid(
            country_code = country_code(country),
            country_name=country
        )
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/data")
def data():
    country = request.args.get('country')
    code = country_code(country)
    covid = db.session.query(DataCovid).all()
    news = make_news('id')
    return render_template(
        "data.html", 
        code=code, 
        country=country, 
        result=result,
        covid=covid,
        news=news
        )

@app.route("/why")
def why():
    return render_template(
        "info.html"
        )

@app.route("/delete")
def delete():
    id = request.args.get('id')
    book_to_delete = DataCovid.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

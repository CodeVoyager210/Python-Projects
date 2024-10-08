from flask import Flask, render_template, redirect, url_for, request
from flask.cli import FlaskGroup
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Optional
import requests
API_KEY = '8c070ca5f791c931ca8682a65bc7fc1d'
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
# CREATE TABLE
class Movie(db.Model):
    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column()
    year : Mapped[int] = mapped_column()
    description : Mapped[str] = mapped_column()
    rating : Mapped[float] = mapped_column(nullable=True)
    ranking : Mapped[int] = mapped_column(nullable=True)
    review : Mapped[str] = mapped_column(nullable=True)
    img_url : Mapped[str] = mapped_column(nullable=True)

with app.app_context():
    db.create_all()
class UpdateForm(FlaskForm):
    rating = StringField(validators=[DataRequired()])
    review = StringField(validators=[DataRequired()])
    submit = SubmitField(name='Done')
class AddMovie(FlaskForm):
    movie_title = StringField(validators=[DataRequired()])
    submit = SubmitField(name='Add')
@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html",movies=movies)
@app.route('/edit',methods=['POST','GET'])
def edit():
    form = UpdateForm()
    if form.validate_on_submit():
        num_id = request.args.get('id')
        new_rating = form.rating.data
        new_review = form.review.data
        movie_change = db.session.execute(db.select(Movie).filter_by(id=num_id)).scalar_one()
        movie_change.rating = new_rating
        movie_change.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',form=form)
@app.route("/delete")
def delete():
    num_id = request.args.get('id')
    movie_delete = db.session.execute(db.select(Movie).filter_by(id=num_id)).scalar_one()
    db.session.delete(movie_delete)
    db.session.commit()
    return redirect(url_for('home'))
@app.route("/add",methods=['POST','GET'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_name = form.movie_title.data
        url = f'https://api.themoviedb.org/3/search/movie?query={movie_name}&api_key={API_KEY}'
        response = requests.get(url=url).json()
        return render_template('select.html',datas=response['results'])

    return render_template('add.html',form=form)
@app.route("/add_database")
def add_database():
    movie_id = request.args.get('id')
    movie_name = request.args.get('title')
    movie_year = request.args.get('year')
    description = request.args.get('desc')
    poster = request.args.get('img')
    img_url = f'https://image.tmdb.org/t/p/original{poster}'
    new_movie = Movie(title=movie_name,year=movie_year,description=description,img_url=img_url)
    db.session.add(new_movie)
    db.session.commit()
    num_id = db.session.execute(db.select(Movie).filter_by(title=movie_name)).scalar_one().id
    return redirect(url_for('edit',id=num_id))
if __name__ == '__main__':
    app.run()

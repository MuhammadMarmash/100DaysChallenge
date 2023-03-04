from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TopTenMovies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


class EditForm(FlaskForm):
    new_rating = StringField('Your Rating Out of 10 e.g.7.5', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    new_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    # db.create_all()
    # db.session.add(Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
    #                 "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with "
    #                 "the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # ))
    # db.session.commit()
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    length = len(all_movies)
    for i in range(length, 0, -1):
        print(i)
        all_movies[i-1].ranking = length - i + 1
        db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500'
    api_key = "670a934885c330414d0635cc1c72a9bc"
    movie_id = request.args.get('id')
    if movie_id is None:
        form = AddForm()
        form.validate_on_submit()
        if form.validate_on_submit():
            title = request.form["new_title"]
            response = requests.get("https://api.themoviedb.org/3/search/movie", params={
                "api_key": api_key,
                "query": title
            })
            response.raise_for_status()
            data = response.json()
            data = data["results"]
            return render_template("select.html", data=data)
        return render_template("add.html", form=form)
    else:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params={
            "api_key": api_key,
            "language": "en-US"
        })
        response.raise_for_status()
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            img_url=f"{TMDB_IMAGE_URL}{data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    form.validate_on_submit()
    movie_id = request.args.get('id')
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = request.form["new_rating"]
        movie_to_update.review = request.form["new_review"]
        db.session.commit()
        return redirect(url_for('home'))
    movie_selected = Movie.query.get(movie_id)
    return render_template("edit.html", movie=movie_selected, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

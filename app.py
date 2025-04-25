from flask import Flask, render_template, redirect, url_for, flash
from forms import AddMovieForm
from config import Config
from models import db, Movie

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    form = AddMovieForm()
    movies = Movie.query.all()

    if form.validate_on_submit():
        movie = Movie(
            title = form.title.data,
            genre = form.genre.data,
            year = form.year.data,
            rating = form.rating.data,
            watched = form.watched.data
        )

        db.session.add(movie)
        db.session.commit()
        flash("Movie added.")
        return redirect(url_for("home"))

    return render_template("index.html", form=form, movies=movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = AddMovieForm(obj=movie)

    if form.validate_on_submit():
        movie.title = form.title.data
        movie.genre = form.genre.data
        movie.year = form.year.data
        movie.rating = form.rating.data
        movie.watched = form.watched.data
        db.session.commit()
        flash("Edited successfully. ✏️")
        return redirect(url_for("home"))

    return render_template("edit_movies.html", form=form, movie=movie)

@app.route("/delete/<int:movie_id>", methods=["POST"])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash("Deleted successfully.🗑")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
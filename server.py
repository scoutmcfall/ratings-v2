"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
        """View homepage."""
        
        return render_template('homepage.html')
# Replace this with routes and view functions!

@app.route('/movies')
def movie_page():
    """view all movies."""
    
    movies = crud.return_all()
    
    return render_template("all_movies.html", movies = movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """show particular movie detail"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie = movie)

# @app.route('/users')
# def 




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)

    app.run(debug=True)
 #app.run(host="0.0.0.0", debug=True)
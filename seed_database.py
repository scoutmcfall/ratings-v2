"""Drop database/createdatabase/create tables/populate database w/data--using data from data/movies.json to create movies
& create 10 rando users; for each user, create 10 ratings on random movies with random scores"""

import os
import json
from random import choice, randint
from datetime import datetime
import crud, model, server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title, overview, poster_path = (
        movie['title'],
        movie['overview'],
        movie['poster_path'],
    )
    release_date = datetime.strptime(movie['release_date'],'%Y-%m-%d')
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
# >>> date_str = "31-Oct-2015"
# >>> format = "%d-%b-%Y"
# >>> date = datetime.strptime(date_str, format)
    # TODO: create a movie here and append it to movies_in_db
    
    
    for n in range(10):
        email = f'user{n}@test.com'  # Voila! A unique email!
        password = 'test'

    # TODO: create a user here
        user = crud.create_user(email, password)
    # TODO: create 10 ratings for the user
        for _ in range(10):
            random_movie = choice(movies_in_db)
            score = randint(1, 5)
            crud.create_rating(user, random_movie, score)
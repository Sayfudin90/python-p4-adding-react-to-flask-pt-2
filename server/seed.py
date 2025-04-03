#!/usr/bin/env python3

from app import app, db
from models import Movie

with app.app_context():
    print("Deleting existing movies...")
    Movie.query.delete()
    
    print("Creating movies...")
    movies = [
        Movie(title="The Shawshank Redemption", year=1994, genre="Drama"),
        Movie(title="The Godfather", year=1972, genre="Crime"),
        Movie(title="The Dark Knight", year=2008, genre="Action"),
        Movie(title="Pulp Fiction", year=1994, genre="Crime"),
        Movie(title="Forrest Gump", year=1994, genre="Drama"),
    ]
    
    db.session.add_all(movies)
    db.session.commit()
    
    print("Movies seeded successfully!")
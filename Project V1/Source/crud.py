"""CRUD operations."""

from model import db, User, connect_to_db
from flask import Flask, render_template, request, redirect

#Write out task list functions for adding task to list
#Add a function to read a task from the list

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def write_task():
    """Write new task to tasks table"""
    title = request.form['title']
    description = request.form['description']

    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()


# def get_duration_from_user(timer_type):
#     # Get input from the user for the duration, as a string
#     duration_minutes = int(input(f"How many minutes will this {timer_type} be?: "))

#     # Create a timedelta object representing user's chosen duration
#     # duration_timedelta = timedelta(minutes=duration_minutes)

#     return duration_timedelta



# def create_movie(title, overview, release_date, poster_path):
#     """Create and return a new movie."""

#     movie = Movie(
#         title=title,
#         overview=overview,
#         release_date=release_date,
#         poster_path=poster_path,
#     )

#     return movie


# def get_movies():
#     """Return all movies."""

#     return Movie.query.all()


# def get_movie_by_id(movie_id):
#     """Return a movie by primary key."""

#     return Movie.query.get(movie_id)


# def create_rating(user, movie, score):
#     """Create and return a new rating."""

#     rating = Rating(user=user, movie=movie, score=score)

#     return rating


# def update_rating(rating_id, new_score):
#     """ Update a rating given rating_id and the updated score. """
#     rating = Rating.query.get(rating_id)
#     rating.score = new_score

if __name__ == "__main__":
    from server import app

    connect_to_db(app)

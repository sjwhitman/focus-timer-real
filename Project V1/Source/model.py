"""Models for movie ratings app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    ratings = db.relationship("Rating", back_populates="user")
    timers = db.relationship("Timer", back_populates="user")
    tasks = db.relationship("Task2", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Timer(db.Model):
    """A task."""

    __tablename__ = "Task"

    #PK and FKs
    timer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    timer_type = db.Column(db.String(10), nullable=False)

    #these two variables store an interval of time
    start_time = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    time_delta = end_time - start_time

    # Define a relationship with User model (assuming User is the name of the user model)
    user = db.relationship('User', back_populates='timers')
    

class Task(db.Model):
    """A task."""

    __tablename__ = "Task"

    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    estimated_duration_start = db.Column(db.DateTime(timezone=True))
    estimated_duration_end = db.Column(db.DateTime(timezone=True))
    time_delta = estimated_duration_end - estimated_duration_start
    task_description = db.Column(db.String(200))

    # Define a relationship with User model (assuming User is the name of the user model)
    user = db.relationship('User', back_populates='tasks')

    def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)


# class Movie(db.Model):
#     """A movie."""

#     __tablename__ = "movies"

#     movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     title = db.Column(db.String)
#     overview = db.Column(db.Text)
#     release_date = db.Column(db.DateTime)
#     poster_path = db.Column(db.String)

#     ratings = db.relationship("Rating", back_populates="movie")

#     def __repr__(self):
#         return f"<Movie movie_id={self.movie_id} title={self.title}>"


# class Rating(db.Model):
#     """A movie rating."""

#     __tablename__ = "ratings"

#     rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     score = db.Column(db.Integer)
#     movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

#     movie = db.relationship("Movie", back_populates="ratings")
#     user = db.relationship("User", back_populates="ratings")

#     def __repr__(self):
#         return f"<Rating rating_id={self.rating_id} score={self.score}>"



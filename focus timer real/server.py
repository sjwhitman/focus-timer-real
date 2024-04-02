from flask import Flask, render_template, request, session, redirect, flash, jsonify
from model import db, connect_to_db

app = Flask(__name__)
app.secret_key = "dev"

@app.route("/")
def homepage():
    """View homepage."""
    return render_template('homepage.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    # app.app_context().push()
# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g

app = Flask("app")

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()



# Each @app.route(...) indicates a URL.
# Using that URL causes the function immediately after the @app.route(...) line to run.
# THIS ROUTE IS TO PROVE THE FLASK SETUP WORKS.
# YOU SHOULD REPLACE IT WITH YOUR OWN CONTENT.
@app.route("/")
def index():
    return render_template('homepage.html')

#Code generated using ChatGPT
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check whether the user name and password match
    if username in users and users[username] == password:
        # If login successful, redirects to user profile page
        return redirect(url_for('user_profile', username=username))
    else:
        # If login failed, redirects back to the login page, and displays an error message
        error = 'Invalid username or password'
        print("please enter valid username and password" )
        return redirect(url_for('index', error=error))
    
@app.route("/user/<username>")
def user_profile(username):
    return render_template('users.html')

@app.route("/Benugo")
def Benugo():
    return render_template('Benugo.html')


@app.route("/restaurantlist")
def restaurantlist():
    return render_template('restaurantlist.html')
    
'''comments={1:"The restaurant is very beautiful for me to hold birthday party after school",2:"Too delicious!"}

# A dictionary for storing comments
def get_comment():
    return{1:"comment1",2:"comment2"}

def your_route():
    comments=get_comment
    return render_template("Benugo.html",comments=comments)

# Render comment page
@app.route('/Benugo')
def benugo():
    return render_template('Benugo.html', comments=get_comment())

# Handles requests to add comments
@app.route('/add_comment', methods=['GET','POST'])
def add_comment():
    if request.method == 'POST':
        comment_content = request.form.get('comment')
        comment_dict = get_comment()
        comment_id = len(comment_dict) + 1
        comment_dict[comment_id] = comment_content
    return redirect('/Benugo')
'''

@app.route("/test")
def test():
    return render_template('test.html')


### YOUR CODE GOES HERE ###
if __name__ == "__main__":
    app.run(debug=True)



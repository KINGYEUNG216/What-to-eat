import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g

app = Flask("app")

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

if __name__ == "__main__":
    app.run(debug=True)
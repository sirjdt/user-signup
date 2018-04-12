from flask import Flask, request, redirect, render_template
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST', 'GET'])
def validate_signup():
    username_error = ''
    password_error = ''
    passwordverify_error = ''
    email_error = ''

    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        passwordverify = request.form["passwordverify"]
        email = request.form["email"]
    
    if username == '':
        username_error = "That's not a vaild username"
    elif len(username) > 20 or len(username) < 3 or ' ' in username:
        username_error = "That's not a vaild username"

    if password == '':
        password_error = "That's not a valid password"
    elif len(password) > 20 or len(password) < 3 or ' ' in password:
        password_error = "That's not a vaild password"

    if passwordverify == '':
        passwordverify_error = "That's not a valid password"
    elif passwordverify != password:
        passwordverify_error = "That's not a valid password"
            
    if (email) and len(email) > 1 and len(email) > 20 or len(email) < 3:
        email_error_1 = "That's not a valid email"
    else:
        if (email) and len(email) > 0:
            if (email) and '@' not in (email.strip()):
                email_error = "That's not a valid email" 
            if (email) and '.' not in (email.strip()): 
                email_error = "That's not a valid email"
            if (email) and " " in (email.strip()):
                email_error = "That's not a valid email"

            


    if username_error == email_error == passwordverify_error == '':
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username = username, email = email, username_error = username_error, password_error = password_error, passwordverify_error = passwordverify_error, email_error = email_error)

    return render_template('index.html')

app.run()
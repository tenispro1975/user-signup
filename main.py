from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
    <style>
    .error {color: #FF0000;}
    </style>
    </head>
        <body>
            

            <form action="/welcome", method="post">
                <p style="font-size: 75;"><b>Signup<b></p>         
                    Username <input type="text" name="Username"/><br>
                    <span class="error"><username_Err;></span>
                    Password <input type="text" name="Password"/><br>
                    <span class="error"><password_Err;></span>
                    Verify Pasword <input type="password name="Verify Password"/><br>
                    <span class="error"><verify_password_err;></span>
                    Email (optional) <input type="text" name="Email (optional)"/><br> 
                    <span class="error"><email_err;></span>
                    <input type="Submit"/> 
            </form>
        </body>
</html>
"""
def empty_text(string):
    if string == " ":
        return False
    return True


@app.route("/")
def validate_info():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify password']
    email = request.form['email']

    username_err = ''
    password_err = ''
    verify_password_err = ''
    email_err = ''

    if not isalpha(username):
         username_err = 'Not valid format'
         username = ''
    else:
        if username not in range(3-20):
            username_err = 'Username value out of range(3-20)'
            username = ''

    if not isalpha(password):
        password_err = 'Not valid format'
        password = ''
    else:
        if password not in range(3-20):
            password_err = 'Password value out of range(3-20)'
            password = ''

    if not isalpha(verify_password):
        verify_password_err = 'Does not match'
        verify_password = ''
    else:
        if veryfy_password not in range(3-20):
            verify_password_err = 'Password value out of range(3-20)'
            verify_password = ''

    def is_valid(email):
        p_count = 0
        at_count = 0
        for char in email:
            elif char = "":
            elif char is not in range of (3-20):
            elif char does not contain "@":
            elif char == ".":
                p_count = p_count + 1
            elif char == "@":
                at_count = at_count + 1
                return 'Not valid format'           

@app.route("/")
def index():
   return form

@app.route("/welcome", methods=['POST'])
def welcome():
    Username = request.form['Username']
    return '<h1>Welcome ' + cgi.escape(username) + '<h1>'

app.run()

from flask import Flask, request, render_template
import cgi
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('home-page.html')
    return render_template('home-page.html', username ='',username_err = '', password='', password_err = '', verify_password ='', verify_password_err = '', email='', email_err = '')

@app.route("/", methods=['POST'])
def validate_info():

    Username = request.form['Username']
    Password = request.form['Password']
    Verify_password = request.form['Verify password']
    Email = request.form['Email']

    username_err = ''
    password_err = ''
    verify_password_err = ''
    email_err = ''

    if not isalpha(username):
        username_err = 'Not valid format'
        username = ''
        if username == "":
            username_err = 'Please enter a username'
            username = ''
        else:
            if len(username) < 3 or len(username) > 20 or ' ' in username:
                username_err = 'Username not valid'
                username = ''

    if not isalpha(password):
        password_err = 'Not valid format'
        password = ''
        if password == "":
            password_err = 'Please enter a password'  
            password = ''
    else:
        if len(password) < 3 or len(password) > 20 or " " in password:
            password_err = 'Password not valid'
            password = ''

    if not isalpha(verify_password):
        verify_password_err = 'Not valid format'
        verify_password = ''
        if verify_password == "":
            verify_password_err = 'Please verify password' 
            verify_password = ''
    else:
        if not verify_password == password:
            verify_password_err = 'Password does not match'
            verify_password = ''
        
    if len(email) >=1 and (len(email) < 3) or (len(email) > 20) or "@" not in email or "." not in email: 
        email_err= 'Not valid email format'                              
        email = ''
    
    if not username_err and not password_err and not verify_password_err and not email_err:
        template = jinja_env.get_template('welcome.html')
        return render_template(username=username)

    else:
        template = jinja_env.get_template('home-page.html')
        return render_template(username_err=username_err, password_err=password_err, verify_password_err=verify_password_err, email_err=email_err, username=username, password=password, verify_password=verify_password, email=email)

#def is_valid(email):
    #if len(email) >=1 and len(email) < 3 or len(email) > 20 or "@" not in email or "." not in email: 
        #email_er r= 'Not valid email format'                              
        #email = ''
        #elif email does not contain  "@":               
            #return 'Not valid format'
    #elif char == ".":
       # p_count = p_count + 1
       #return 'Not valid format'
    #elif char == "@":
        #at_count = 1
        #return True
        #at_count = at_count + 1
        #return 'Not valid format'           

@app.route("/welcome", methods=['POST'])
def welcome():  
    username=request.form['username']
    template = jinja_env.get_template('welcome.html')
    return render_template('welcome.html', username=username)

app.run()

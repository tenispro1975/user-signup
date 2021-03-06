from flask import Flask, request, render_template

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    username=""
    username_err=""
    password=""
    password_err=""
    verify_password=""
    verify_password_err=""
    email=""
    email_err=""

    return render_template('home-page.html', username=username, username_err=username_err, password=password, password_err=password_err, verify_password=verify_password, verify_password_err=verify_password_err, email=email, email_err=email_err)

@app.route("/", methods=['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_err = ''
    password_err = ''
    verify_password_err = ''
    email_err = ''

    #if not isalpha(username):
        #username_err = 'Not valid format'
       #username = ''
    #else:
    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_err = 'Username not valid'
        username = ''

    #if not isalpha(password):
        #password_err = 'Not valid format'
        #password = ''
    #else:
    if len(password) < 3 or len(password) > 20 or " " in password:
        password_err = 'Password not valid'
        password = ''
    
    if not verify_password == password:
        verify_password_err = 'Password does not match'
        verify_password = ''
        
    if email == '':
        email = ''
   
    else:
        if len(email) >=1 and (len(email) < 3) or (len(email) > 20) or "@" not in email or "." not in email: 
            email_err= 'Not valid email format'                              
            email = ''
    
        #if email == '':
            #email = ''


    if not username_err and not password_err and not verify_password_err and not email_err:
        return render_template('welcome.html', username=username)

    else: 
        return render_template('home-page.html', username=username, username_err=username_err, password=password, password_err=password_err, verify_password=verify_password, verify_password_err=verify_password_err, email=email, email_err=email_err)

app.run()

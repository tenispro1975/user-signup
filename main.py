from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
    
    </head>
        <body>
            <form action="/welcome" method="POST">
                <p style="font-size: 20;"><b>Signup<b></p>
                <div>
                    <label for="Username">Username</label>
                    <input id="name" type="text" name="Username"/>
                </div>
                <br>
                <div> 
                    <label for="Password">Password</label>
                    <input type="password" name="Password"/>
                </div>
                <br>
                <div>
                    <label for="Verify-Password">Verify Password</label>
                    <input type ="password" name="Verify-Password"/>
                </div>
                <br>
                    <label for="Email-(Optional)">Email (Optional)</label>
                    <input type="text" name="Email (Optional)"/>
            </label>
            <br>
            <label>
                <input type="Submit" name="Submit Query"/>
            </label>  
        </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/welcome", methods=['POST'])
def welcome():
    name = request.form['name']
    return '<h1>Welcome ' + name + '<h1>'


app.run()

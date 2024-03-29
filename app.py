# import the flask module form the flask library
from flask import Flask, render_template, request

# assign name 'app' to flask app
app = Flask(__name__)

# render specified html files for given URL addresses
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/katrina')
def katrina():
    return render_template('katrina.html')

@app.route('/keepintouch')
def keepintouch():
    return render_template('keepintouch.html')

@app.route('/sarah')
def sarah():
    return render_template('sarah.html')

@app.route('/ouradventures')
def ouradventures():
    return render_template('ouradventures.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# run the app with debug mode on if name = __main__  (the __Main__ is a convention)
if __name__ == '__main__':
    app.run(debug=True)

# import the flask module form the flask library
from flask import Flask, render_template

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



# run the app with debug mode on if name = __main__  (the __Main__ is a convention)
if __name__ == '__main__':
    app.run(debug=True)

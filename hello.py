from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/katrina')
def katrina():
    return render_template('katrina.html')

@app.route('/sarah')
def sarah():
    return render_template('sarah.html')

if __name__ == '__main__':
    app.run(debug=True)
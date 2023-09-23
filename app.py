from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == "__main__":
    app.run(debug=True)
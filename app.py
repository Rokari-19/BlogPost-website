from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)



POSTS = [
    {
        'id':'1',
        'class':'food',
        'content':'lorem ipsum',
        'header':'lorem ipsuck my titties'
    },

    {
        'id':'2',
        'class':'food',
        'content':'lorem ipsum',
        'header':'lorem ipsuck my titties'
    },

    {
        'id':'3',
        'class':'food',
        'content':'lorem ipsum',
        'header':'lorem ipsuck my titties'
    },

    {
        'id':'4',
        'class':'food',
        'content':'lorem ipsum',
        'header':'lorem ipsuck my titties'
    },

    {
        'id':'5',
        'class':'food',
        'content':'lorem ipsum',
        'header':'lorem ipsuck my titties'
    }
]

@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/write')
def welcome():
    return render_template('write.html', data=POSTS)

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/data')
def get_post():
    return jsonify(POSTS)

if __name__ == "__main__":
    app.run(debug=True)
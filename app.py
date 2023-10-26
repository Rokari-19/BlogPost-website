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

@app.route('/index')
def index():
    return render_template('index.html', data = POSTS)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/details')
def post_details():
    return render_template('post-details.html', data=POSTS)

@app.route('/blog')
def blog():
    return render_template('blog.html', data=POSTS)

@app.route('/data')
def get_post():
    return jsonify(POSTS)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
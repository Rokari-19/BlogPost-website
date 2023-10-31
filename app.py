from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)



POSTS = [
    {
        'id':'1',
        'class':'food',
        'content':'lorem ipsum',
        'header':'food1'
    },

    {
        'id':'2',
        'class':'food',
        'content':'lorem ipsum',
        'header':'food2'
    },

    {
        'id':'3',
        'class':'food',
        'content':'lorem ipsum',
        'header':'food3'
    },

    {
        'id':'4',
        'class':'food',
        'content':'lorem ipsum',
        'header':'food4'
    },

    {
        'id':'5',
        'class':'food',
        'content':'lorem ipsum',
        'header':'food5'
    }
]

JOBS = [
    {
        'id':1, 
        'title':'Backend developer',
        'location':'Abuja, Nigeria',
        # 'Wages/Hour':'negotiable',
        'member': 'Ajiri "rokari" iyelobu',
        'github': 'https://github.com/rokarioss'
    }, 
    # {
    #     'id':2, 
    #     'title':'Data Scientist',
    #     'location':'Abuja, Nigeria',
    #     # 'Wages/Hour':'negotiable',
    #     'member': 'anosike ugochukwu'
    # },
    {
        'id':3, 
        'title':'Front End Engineer',
        'location':'Uke, Nigeria',
        # 'Wages/Hour':'negotiable',
        'member': 'Daniel "kng-koder" fori',
        'github': 'https://github.com/DFori'

    },
    {
        'id':4, 
        'title':'Fullstack Developer',
        'location':'remote',
        # 'Wages/Hour':'negotiable',
        'member': 'Aigbona Benjamin "bencool"',
        'github':'https://github.com/aigbonabenjamin'
    }
    
]

SERV = [
    {
        'id':1,
        'title':'Website development',
        'price':'Negotiable',
        'duration':'Depending on customer terms'
    },
    {
        'id':2,
        'title':'Back-end data-base management',
        'price':'Negotiable',
        'duration':'Depending on payment'
    },
    {
        'id':3,
        'title':'Cyber Security & IT-support services',
        'price':'Negotiable',
        'duration':'Depends on price'
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
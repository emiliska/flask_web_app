from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

# objects
app = Flask(__name__)
bootstrap = Bootstrap(app)

# posts
posts=[
    {
        'author': 'Emily Eubanks',
        'title': 'Blog Post 1',
        'content': 'First post created',
        'date_posted': 'January 29, 2020'
    },{
        'author': 'Emily Eubanks',
        'title': 'Blog Post 1',
        'content': 'First post created',
        'date_posted': 'January 29, 2020'
    }
]


# Error Messages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Routes

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html',
            posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


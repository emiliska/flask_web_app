from flask import Flask, render_template, url_for
from datetime import datetime
from flask_moment import Moment

# objects
app = Flask(__name__)

# Dummy Data for Fake Blog Posts
posts = [
        {
            'author': 'Emily Eubanks',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'January 29, 2020'
        },
        {
            'author': 'Emily Eubanks',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'January 28, 2020'
        }
]

# Error Messages


# Routes

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', 
            posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


# first app is the main folder name
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'prem'}
    posts= [
        { 
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        { 
            'author': {'username': 'Suasan'},
            'body': 'The Avengers movie was so cool'
        }
        ]
    return render_template('index.html', title='Home' , user=user, posts = posts)
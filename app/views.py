from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    popular_movies = get_movies('popular')
    print(popular_movies)
    return render_template('index.html',top_headlines)
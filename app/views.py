from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():
    news = get_news()

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html',articles=news )
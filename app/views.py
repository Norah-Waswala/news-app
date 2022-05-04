from flask import render_template
from app import app
from .request import get_news,sources,get_articles


@app.route('/')
def index():
    news = get_news()
    source=sources("sources")
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html',articles=news,sources=source )

@app.route("/articles/<name>")
def body(name):
    bbc=get_articles("abc-news")
    abc=get_articles("abc-news-au")
    aljezera=get_articles("al-jazeera-english")
    technica=get_articles("ars-technica")

    return render_template("articles.html",name=name,bbc_news=bbc,abc_news=abc,aljezera_n=aljezera,tech=technica)

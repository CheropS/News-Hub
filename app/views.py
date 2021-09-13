from flask import render_template
from app import app 
from .request import get_news, get_new, get_articles

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #getting general news
    general_news=get_news('general')
    sports_news=get_news('sports')
    technology_news=get_news('technology')

    title='Welcome to the Best Source for News and Articles'
    return render_template('index.html', title=title, general=general_news, sports=sports_news, technology=technology_news )

@app.route('/news/<string:news_id>')
def news(news_id):
    '''
    View news page function that return news details and its data
    '''
    source_news=get_new(news_id)
    for s in source_news:
        print(s.title)

    name=f'{news_id}'

    return render_template('news.html', name=name, source_news=source_news)

#getting articles 


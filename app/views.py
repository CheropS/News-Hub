from flask import render_template
from app import app 
from .request import get_news

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

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page funciton that return news details and its data
    '''
    return render_template('news.html', id=news_id)

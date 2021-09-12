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
    print(general_news)
    title='Welcome to the Best Source for News and Articles'
    return render_template('index.html', title=title, general=general_news)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page funciton that return news details and its data
    '''
    return render_template('news.html', id=news_id)

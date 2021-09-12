from flask import render_template
from app import app 

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title='Welcome to the Best Source for News and Articles'
    return render_template('index.html', title=title)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page funciton that return news details and its data
    '''
    return render_template('news.html', id=news_id)

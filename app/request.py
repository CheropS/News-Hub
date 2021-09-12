import os
from app import app
import urllib.request,json
from .models import news 

News=news.News


#getting API key
api_key=os.environ.get('NEWS_API_KEY')

#getting the news base url
base_url=app.config['NEWS_API_BASE_URL']
news_search_url=app.config['NEWS_SEARCH_URL']

def get_news(category):
    '''
    function that gets json response to our url
    '''
    get_news_url=base_url.format(category, api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)

        news_result=None

        if get_news_response['sources']:
            news_result_list=get_news_response['sources']
            news_result=process_news(news_result_list)

    return news_result

def process_news(news_list):
    '''
    Function that processes news articles and processes it into a list

    Args: A list of news that make up a dictionary

    Returns: 
        news_result: A list of news objects
    '''
    
    news_result=[]
    for news_item in news_list:
        id=news_item.get('id')
        name=news_item.get('name')
        description=news_item.get('description')
        url=news_item.get('url')
        category=news_item.get('category')
        language=news_item.get('language')
        country=news_item.get('country')

        new_source=News(id, name, description, url, category, language, country)
        news_result.append(new_source)
    
    return news_result

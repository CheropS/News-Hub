from app import app
import urllib.request,json
from .models import news 

News=news.News


#getting API key
api_key=app.config['NEWS_API_KEY']

#getting the news base url
base_url=app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    function that gets json response to our url
    '''
    get_news_url=base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)

        news_result=None

        if get_news_response['results']:
            news_result_list=get_news_response['results']
            news_result=process_results(news_result_list)

    return news_result

def process_results(news_list):
    '''
    Function that processes news results and processes it into a list'''
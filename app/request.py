import os
from app import app
import urllib.request,json
from .models import News, Articles



#getting API key
api_key=os.environ.get('NEWS_API_KEY')

#getting the news base url
base_url=app.config['NEWS_API_BASE_URL']
news_search_url=app.config['NEWS_SEARCH_URL']
headline_url=app.config['NEWS_HEADLINE_URL']

def get_news(category):
    '''
    function that gets json response to our url
    '''
    get_news_url=base_url.format(category, api_key)
    

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

def get_new(news_id):
    '''
    function that gets json response to our url
    '''
    get_news_details_url=headline_url.format(news_id, api_key)
    print(get_news_details_url)
    

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data=url.read()
        news_details_response=json.loads(news_details_data)

        news_object=None
        news_object_list=[]

        print(news_details_response)
        
        if news_details_response:
            

            source=news_details_response.get('source')
            author=news_details_response.get('author')
            title=news_details_response.get('title')
            description=news_details_response.get('description')
            url=news_details_response.get('url')
            urlToImage=news_details_response.get('urlToImage')
            published=news_details_response.get('published')
            content=news_details_response.get('content')

            news_object=Articles(source, author, title, description, url, urlToImage, published, content)
            news_object_list.append(news_object)

            for n in news_object_list:
                print(n.title)

        

    return news_object_list


def get_articles():
    '''Function that gets news articles from the url
    '''
    get_articles_url=headline_url.format(os.name, api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data=url.read()
        get_articles_response=json.loads(get_articles_data)

        news_result=None

        if get_articles_response['source']:
            articles_result_list=get_articles_response['sources']
            articles_result=process_articles(articles_result_list)

    return articles_result

def process_articles(articles_list):
    '''
    Function that processes news articles and processes it into a list

    Args: A list of articles that make up a dictionary

    Returns: 
        articles_result: A list of articles objects
    '''
    
    articles_result=[]
    for articles_item in articles_list:
        id=[]
        name=articles_item.get('name')
        author=articles_item.get('author')
        title=articles_item.get('title')
        description=articles_item.get('description')
        url=articles_item.get('url')
        
        new_article=News(id, name, author, title, description, url)
        articles_result.append(new_article)
    
    return articles_result

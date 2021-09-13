class News:
    '''news class to define news object
    '''

    def __init__(self, id, name, description, url, category, language, country):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        self.language=language
        self.country=country

class Articles:
    '''
    This is an articles class that defines articles object
    '''

    def __init__(self, source, author, title, description, url, urlToImage, published, content):
        self.source=source
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.published=published
        self.content=content 
       
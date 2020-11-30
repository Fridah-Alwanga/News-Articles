import os

class Config:
    '''
    General configuration parent class
    '''
    # NEWS_API_BASE_URL ='https://api.thenewsdb.org/3/news/{}?api_key={}'
    SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = ('fridah')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

import requests
from config import Config
from .models import Quotes
import urllib.request,json

random_quotes = None
popular_quotes = None


def configure_request(app):
    global random_quotes,popular_quotes

    random_quotes = app.config['RANDOM_QUOTES']
    popular_quotes = app.config['POPULAR_QUOTES']

    
          

def getQuotes():
    random_quote = requests.get(random_quotes)
    with urllib.request.urlopen(random_quote) as url:
        random_quote_data = url.read()
        random_quote_response = json.loads(random_quote_data)

        random_results = None

        if random_quote_response['random']:
            random_results_list = random_quote_response['random']
            random_results = process_results(random_results_list)
    
    return random_results

def process_results(quotes_list):
    random_results=[]
    for quote in quotes_list:
        id=quote.get('id')
        author=quote.get('author')
        quote=quote.get('quote')
        
        url=quote.get('url')

        if name!=('ANSA.it'):
            quote_object=Quotes(id,author,quote)

            random_results.append(quote_object)
    return random_results

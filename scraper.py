import requests
from bs4 import BeautifulSoup, SoupStrainer
from pandas import DataFrame as df

def get_table_from(url):

    '''Returns a BeautifulSoup ResultSet object containing all the 'tr' tags on the requested URL.

    Does some simple checking to ensure provided URL is in fact valid for BoxOfficeMojo only.''' 

    if 'boxofficemojo.com' in url:
        
        identifier = '#dcdcdc'
        strainer = BeautifulSoup(requests.get(url).text,parse_only=SoupStrainer("table"))
        raw_tables = strainer.find_all(lambda tag: tag.name == 'table' and
                                       tag.tr.has_attr('bgcolor') and
                                       tag.tr['bgcolor'] == identifier)
        return raw_tables

    else:
        raise ValueError('Provided URL is not a boxofficemojo.com URL')

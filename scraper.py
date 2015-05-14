import requests
from bs4 import BeautifulSoup
from pandas import DataFrame as df

def get_table_from(url):

    '''Returns a BeautifulSoup object containing all the 'tr' tags on the requested URL.

    Does some simple checking to ensure provided URL is in fact valid for BoxOfficeMojo only.''' 

    identifier = '#dcdcdc'

    if 'boxofficemojo.com' in url:
        response = requests.get(url)
        raw_tables = BeautifulSoup(response.text).find_all(lambda tag: tag.name == "table" and
                                                       tag.tr.has_attr('bgcolor') and
                                                       tag.tr['bgcolor'] == identifier)
        if len(table) > 1:
            print('More than one table found - please inspect for whichever is appropriate')
        return raw_tables
    else:
        raise ValueError('Provided URL is not a boxofficemojo.com URL')

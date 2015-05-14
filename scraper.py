import requests
from bs4 import BeautifulSoup

def get_table_from(url):

    '''Returns a BeautifulSoup object containing all the 'tr' tags on the requested URL.

    Does some simple checking to ensure provided URL is in fact valid for BoxOfficeMojo only.''' 

    if 'boxofficemojo.com' in url:
        response = requests.get(url)
        soup_object = BeautifulSoup(response.text)
        return soup_object
    else:
        raise ValueError('URL is not a boxofficemojo.com URL')

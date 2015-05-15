import requests
from bs4 import BeautifulSoup, SoupStrainer

def get_table_from(url,clean = True):

    '''Returns a list of list of lists.

    The innermost lists represents rows within a table; the outer lists represents a table.
    The elements of the innermost lists are all strings.

    Does some simple checking to ensure provided URL is in fact valid for BoxOfficeMojo only.''' 

    if 'boxofficemojo.com' in url:
        
        identifier = '#dcdcdc'

        strainer = BeautifulSoup(requests.get(url).text,parse_only=SoupStrainer("table"))

        raw_tables = strainer.find_all(lambda tag: tag.name == 'table' and
                                       tag.tr.has_attr('bgcolor') and
                                       tag.tr['bgcolor'] == identifier)
        
        unwanted_objects = [undesired_object.extract() for table in raw_tables for undesired_object in table(["script","option","table","form"])]
        
        formatted_tables = [[[item.text for item in row.find_all("td")] for row in table.find_all("tr")] for table in raw_tables]
            
        if clean == True:
            return formatted_tables
        else:
            return formatted_tables,unwanted_objects

    else:
        raise ValueError('Provided URL is not a boxofficemojo.com URL')

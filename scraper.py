from bs4 import BeautifulSoup, SoupStrainer
from pandas import DataFrame

def get_table_from(page_html,cleaned = False,stripped=True):

    '''Returns formatted_tables, a list of DataFrame objects corresponding to tables on the page_html corresponding to a BOM page format.

    If that doesn't happen, returns a list of lists. The innermost lists represents rows within a table; the outer lists represents a table.
    The elements of the innermost lists are all strings.

    If cleaned is set to True, the 'clean' utility is called to try to force the table into a DataFrame object. 'clean' is set to False because
    the vast majority of cases on boxofficemojo don't require the extra overhead. 

    This strips a lot of content that might be unwanted. Unwanted content include nested tables, Javascript script and option attributes, and HTML forms.
    If you want to retrieve this content, for whatever reason, set stripped to False, and it will return a list of the unwanted strings along with formatted_tables.''' 

    identifier = '#dcdcdc'

    strainer = BeautifulSoup(page_html,parse_only=SoupStrainer("table"))

    raw_tables = strainer.find_all(lambda tag: tag.name == 'table' and
                                   tag.tr.has_attr('bgcolor') and
                                   tag.tr['bgcolor'] == identifier)
        
    unwanted_objects = [undesired_object.extract() for table in raw_tables
                        for undesired_object in table(["script","option","table","form"])]
        
    formatted_tables = [[[item.text.rstrip('\n') for item in row.find_all("td")]
                         for row in table.find_all("tr")] for table in raw_tables]
        
    try:
        formatted_tables = [DataFrame(table[1:],columns = table[0]) for table in formatted_tables]
    except Exception as ex:
        print("Failed to convert to DataFrame object. Returning as nested list...")
        print("Error returned was: "+str(ex))
        
    if cleaned == True:
        from utilities import clean
        formatted_tables = clean(formatted_tables)

    if stripped == True:
        return formatted_tables
    else:
        return formatted_tables,unwanted_objects

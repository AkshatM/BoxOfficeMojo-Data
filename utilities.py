from pandas import DataFrame

def clean(formatted_tables):

    print("Cleaning and trying to convert to DataFrame...")

    '''Cleans the table as much as possible to convert it into a DataFrame object.

    Use this utility to try to convert nested lists from get_table_from to DataFrame objects.'''

    for table in formatted_tables:

        maximum_length = max((len(item) for item in table))

        if len(table[0]) < maximum_length:
            table[0] = [lone_header_tag for header in table[0] for lone_header_tag in header.split('/')]

    formatted_tables = [DataFrame([row if (len(row) == maximum_length) for row in table[1:]],columns=table[0]) for table in formatted_tables]

    return formatted_tables

        
        
    

# About

BoxOfficeMojo-Data is a set of functions for automating table scraping from BoxOfficeMojo.

If you came here before and are confused about just how much this project has changed, this repository _used_ to house a set of scripts for scraping very particular data from very particular pages (all of those listed under 'Genres') on BoxOfficeMojo. Like all scripts, however, it required immense modifications for even minor deviations from its purpose, made many assummptions about the final desired form of the data, became a series of monolithic files that were _not_ easy to read, and in general was not well designed. This is an attempt to improve BoxOfficeMojo-Data to better meet people's needs.

If you're interested in working with the original version of this repository, it's still here - simply jump to the branch named 'original' in this repository, and pull from there.


# Dependencies

As of now, BoxOfficeMojo-Data functions depend on:

* [Requests](http://docs.python-requests.org/en/latest/)
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](http://pandas.pydata.org/) (in future commits)

# Current Structure

This repository currently contains:
* `scraper.py`, a collection of scraping functions
  * `get_table_from(_url_)` - Takes in a valid BoxOfficeMojo URL and returns a list of raw HTML tables containing data on the URL. To accomplish this task, it looks for all tables whose `tr` contains and attribute `bgcolor = #dcdcdc`. This pattern is consistent across BoxOfficeMojo, and enables easy grouping of all significant tables on the page. 

# Future Improvements

* Return our raw HTML tables as cleverly parsed dataframe objects using `pandas`. Ideally, this would require an internal conversion of the tables to lists within lists, which can be accomplished through list comprehensions and iterations over the elements of the table.
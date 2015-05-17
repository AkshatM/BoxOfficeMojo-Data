# About

BoxOfficeMojo-Data is a set of functions for converting tables from BoxOfficeMojo-like or sourced pages to `pandas` DataFrame objects.

If you came here before and are confused about just how much this project has changed, this repository _used_ to house a set of scripts for scraping very particular data from very particular pages (all of those listed under 'Genres') on BoxOfficeMojo. Like all scripts, however, it required immense modifications for even minor deviations from its purpose, made many assummptions about the final desired form of the data, became a series of monolithic files that were _not_ easy to read, and in general was not well designed. This is an attempt to improve BoxOfficeMojo-Data to better meet people's needs.

If you're interested in working with the original version of this repository, it's still here - simply jump to the branch named 'original' in this repository, and pull from there.

# Caveats

This tool only parses a static HTML doc that corresponds to BoxOfficeMojo web pages, and converts it to a friendlier format. It _cannot_ be used to actually retrieve the pages themselves from a BoxOfficeMojo page. I am not responsible for the legal consequences that might ensue if you _actually_ try to retrieve (manually or automatically) BoxOfficeMojo datasets, which is [against BoxOfficeMojo's Terms of Use](http://www.boxofficemojo.com/about/termsofuse.htm). 

This tool does not qualify as data mining or screen scraping, as it does not faciliate either data retrieval or actual invesitgation of data - it is **only** a parsing utility. It can be used for tables that _simulate_ BoxOfficeMojo format, and thus may be of interest to websites interested in building APIs for similar tables on their website. Those with express legal permission from BoxOfficeMojo for actual content scraping may also use this tool.


# Dependencies

As of now, BoxOfficeMojo-Data functions depend on:

* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](http://pandas.pydata.org/)

# Installation

For now, all you can do is clone this repository somewhere and put both files in your pythonpath. Sorry about that - a future version will probably be released on PyPi, so pip installation will work then, or a setup script will let that happen.

# Current Structure

This repository currently contains:
* `scraper.py`, a collection of parsing functions
   * `get_table_from(page_html, _cleaned_ = False, _stripped_ = True)`

   Returns formatted_tables, a list of DataFrame objects corresponding to tables on the page_html corresponding to a BOM page format.

   If that doesn't happen, returns a list of lists. The innermost lists represents rows within a table; the outer lists represents a table.The elements of the innermost lists are all strings.

   If cleaned is set to True, the 'clean' utility is called to try to force the table into a DataFrame object. 'clean' is set to False because the vast majority of cases on boxofficemojo will convert to DataFrame objects without error and will convert to DataFrame objects without fuss. *Only* use if the result is a nested list rather than a DataFrame object, otherwise risk the penalty for ignoring instructions. 

   This strips a lot of content that might be unwanted. Unwanted content include nested tables, Javascript script and option attributes, and HTML forms. If you want to retrieve this content, for whatever reason, set stripped to False, and it will return a list of the unwanted strings along with formatted_tables.

* `utility.py`, a set of utilities that aid in parsing for complicated table formats. 
   * `clean(formatted_table)`

   Attempts to correct for most common cause of failure of DataFrame conversion in `get_table_from`. Usually, this is because the table column headers span multiple cells while the actual cells below them do not, leading to a mis-match the between the number of columns `pandas` thinks the table should have and the actual number of columns provided to it. 

   To solve this, `clean` simply loops over the first row of each table and converts joined columns (usually columns with '/' in them) into separate individual columns. In most cases, this should suffice to permit conversion to DataFrame.

# Example Usage

Let `page` be our page in raw HTML format. Here's an example table on `page` presented below.

```html
<table border="0" cellspacing="0" cellpadding="5" class="chart-wide">
<tr bgcolor="#dcdcdc">
<td align="center"><font size="2\"><a href="/movies/?page=weekend&id=et.htm&sort=date&order=DESC&p=.htm"><b>Date<br>(click to view chart)</b></a></font></td>
<td align="center"><font size="2"><a href="/movies/?page=weekend&id=et.htm&sort=rank&order=ASC&p=.htm">Rank</a></font></td>
<td align="center"><font size="2"><a href="/movies/?page=weekend&id=et.htm&sort=rank&order=ASC&p=.htm">Movie</a></font></td>
</tr>
<tr bgcolor="#f4f4ff">
<td><nobr><font size="2"><a href="/weekend/chart/?yr=1982&wknd=26&p=.htm"><b>Jun 18&#150;20</b></a></font></nobr></td>
<td align="center"><font size="2">1</font></td>
<td align="center"><font size="2">Bar</font></td>
</tr>
</table>
```

Hard to read, right? No idea what's going on?

We can convert tables on that document to DataFrames by simply running

```python
import scraper

table = scraper.get_table_from(page)
```

and we get, when we call `table` 

```python
[  Date(click to view chart) Rank Movie
0                 Jun 18?20    1   Bar]
```

Then we can convert tables on that document to DataFrames by


```python
import scraper

table = scraper.get_table_from(page)
```

If the function fails to convert the tables to a DataFrame format (it'll provide an error _that doesn't prevent assignment_, so you'll have either a series of nested lists or a DataFrame to work with), you can try running with `cleaned = True` instead.

```python
table = get_table_from(page,cleaned=True)
```

This should solve most problems. `cleaned = True` imports `utilities.py` internally, so please make sure both files are on your Python path. Please post an issue if this does not work for your specific use.

# Extensions

If you aren't interested in using this for BoxOfficeMojo-like pages, you can pretty much also rewrite this for your own specific tables. Probably the only thing you'll need to change is the `identifier` variable in `scraper.py` which identifies the desired table by its attributes.

# About

BoxOfficeMojo-Data is a set of functions for automating table scraping from BoxOfficeMojo.

If you came here before and are confused about just how much this project has changed, this repository _used_ to house a set of scripts for scraping very particular data from very particular pages (all of those listed under 'Genres') on BoxOfficeMojo. Like all scripts, however, it required immense modifications for even minor deviations from its purpose, made many assummptions about the final desired form of the data, became a series of monolithic files that were _not_ easy to read, and in general was not well designed. This is an attempt to improve BoxOfficeMojo-Data to better meet people's needs.

If you're interested in working with the original version of this repository, it's still here - simply jump to the branch named 'original' in this repository, and pull from there.

#Blueprints for Design

BoxOfficeMojo-Data should:
* Be able to handle _all_ major tables that appear on BoxOfficeMojo-Data pages, rather than be limited to specific Genre pages. Support will _not_ be maintained for objects on a BoxOfficeMojo page that doesn't contain a table.
* Intelligently parse through tables on a page, and allow users to decide how to group variables to store in a file.
* Allow users to make use of _utilities_ that can come in handy when storing scraped data.

BoxOfficeMojo's behaviour should resemble that of an API, and make _no_ assumptions about what the user should do with the data. In that regard, it should behave like a proper object-oriented Pythonic library, providing people the flexibility to choose how to handle and treat the data.

# Current Structure

This repository currently contains:
* `scraper.py`, a scraper function that takes in a URL and returns a BeautifulSoup object representing all the `tr` tags within the page. _This will be improved upon in a forthcoming commit, where it should return an object representing the single major page of that list_.

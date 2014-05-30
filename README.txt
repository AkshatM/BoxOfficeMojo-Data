README FOR BOXOFFICEMOJO SCREEN SCRAPER.

Author: Akshat Mahajan

Works only on Python 2.7.6. and below. Can be adjusted for Python 3 and above if you're willing to do the work.

In order to ensure you have correct components, make sure you have the following three modules in place:

1. boxofficemojo.py (author: Claudio Baccigalupo) #retrieves weekly incomes for given movie id
2. download.py (author: Claudio Baccigalupo) #accesses the weekly incomes page via http
3. AppendMovieData.py #identifies list of movie ids from genre directory, scrapes relevant data using boxofficemojo and itself, and reads into appropriate files.
   #currently, all movie data is sorted by month of release
4. Requests library
5. Beautiful Soup 4 library

Files listed with Claudio Baccigalupo as author were taken from https://github.com/claudiob/boxoffice, before I knew how to fork a respository (and now it's too late).

Other components that are not absolutely necessary, but recommended in case of mistakes:

1. DuplicateRemove.py #remove duplicate values from text files
2. Film Count.py #count the number of movies in files in directory

Recommended Instructions:

1. On downloading the screen scraper and necessary modules (.py files) and the data (.txt files) into a suitable folder (called A, for example), MOVE the .py files to a separate folder (say B). 
This is to ensure Film Count.py does not overestimate the number of movies actually contained.

2. Change all the directories within each AppendMovieData.py, DuplicateRemove.py and Film Count.py to A. This ensures proper appending and accounting.

3. To use the screen scraper, identify your target genre directory. An example is provided in AppendMovieData.py. Make careful note of the number of films each page in the genre sub-directory.
This number will allow you to identify how much of the page is to be scripted. Further instructions are provided in AppendMovieData.py. MAKE SURE your internet connection is working.
If internet connection cannot be established, the screen scraper will not work.

4. It is always best to perform quality control. Use DuplicateRemove.py to make sure duplicate records of movies, which can happen if you accidentally run the screen scraper on the same genre directory twice, are not preserved.
Make sure to individually read from one file, but write to a new file separately, for ease of use when using DuplicateRemove.py. You can use Film Count.py at any time to find out how many movies have been scraped.

Please study the .py files themselves to understand how they work. 

Additional Notes: For most purposes, these files will work. However, there are some things it cannot do. It will not scrape weekly incomes for movies on the genre directory with (#insert year here). e.g. Alice in Wonderland (2010) will not be scraped for lifetime weekly income.
However, such movies are small in number, and we can always rewrite the code to specially retrieve these incomes.

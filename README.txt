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

1. Change all the directories within each AppendMovieData.py, DuplicateRemove.py and Film Count.py to A. This ensures proper appending and accounting.

2. To use the screen scraper, identify your target genre directory. An example is provided in AppendMovieData.py. Make careful note of the number of films each page in the genre sub-directory.
This number will allow you to identify how much of the page is to be scripted. Further instructions are provided in AppendMovieData.py. MAKE SURE your internet connection is working.
If internet connection cannot be established, the screen scraper will not work.

3. It is always best to perform quality control. Use DuplicateRemove.py to make sure duplicate records of movies, which can exist if you accidentally run the screen scraper on the same genre directory twice, are not preserved.
Make sure to individually read from one file, but write to a new file separately, for ease of use when using DuplicateRemove.py. You can use Film Count.py at any time to find out how many movies have been scraped.

Please study the .py files themselves to understand how they work. 

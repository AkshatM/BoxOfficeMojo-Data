import requests
import os
from bs4 import BeautifulSoup
import string

path = r'C:\Users\Akshat Mahajan\Desktop\Data' #change file name to where you want your data to be saved.

# The data returned by this code consists (in order) of movie name, lifetime gross, opening weekend box office revenue,
# and then the weekly box office revenue, stretching as long as BoxOfficeMojo holds the data.

print 'Initialising...'

L = []

#edit the argument in requests.get() to your target genre directory - otherwise this will scrape the wrong thing. 
#Example is provided below.

r = requests.get('http://www.boxofficemojo.com/seasonal/?view=releasedate&yr=2015&season=Summer')

soup = BeautifulSoup(r.text)

print 'Retrieved table on desired web page...'
    
print 'Process finished'

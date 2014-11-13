import requests
import os
from bs4 import BeautifulSoup
from boxofficemojo import retrieve_incomes
import string
import calendar

path = r'C:\Users\Akshat Mahajan\Desktop\Data' #change file name to where you want your data to be saved.
os.chdir(path)

# The data returned by this code consists (in order) of movie name, lifetime gross, opening weekend box office revenue,
# and then the weekly box office revenue, stretching as long as BoxOfficeMojo holds the data.
print 'Initialising...'
L = []

MatrixArray = [[] for i in range(12)]
checklist = []
for i in range(1,13):
    checklist.append(str(i)+'/')
CalendarList = [calendar.month_name[i] for i in range(1,13)]

#edit the argument in requests.get() to your target genre directory - otherwise this will scrape the wrong thing. 
#Example is provided below.

r = requests.get('http://www.boxofficemojo.com/genres/chart/?view=main&sort=gross&order=DESC&pagenum=1&id=foreign.htm')
soup = BeautifulSoup(r.text)
print 'Retrieved desired web page...'
#findid basically finds you theboxoffice movie id to plug into retrieve_incomes. It's written so that pesky 
#characters in brackets (e.g. name of the country movie comes from) will be ignored. Code, however, will ignore numerical 
#characters (e.g. Alice in Wonderland (2010)), as BoxOfficeMojo inevitably incorporates year of release into its movie id list,
# in the event of multiple movies sharing the same name, and without the year, hunting for the ids will return nothing.
def findid(n):
    if str(n).endswith(')'):
        try:
            int(n[str(n).find('(')+1:-1])
            m = str(n)
        except ValueError:
            m = str(n)[:str(n).find('(')]
        for link in soup.findAll('a', href=True, text=str(m)):
            return link['href'][12:-4]
    else:
        for link in soup.findAll('a', href=True, text=str(n)):
            return link['href'][12:-4]

for line in soup("tr"):
    L.append(line.get_text())
print 'Parsing...'

for x in L[4:76]:#change slice to 4:104 unless number of movies on page less than 100; then change 104 to 'number of movies' + 4 in the page you're scraping
    y = str(x).split('\n')
    for m in checklist: 
        if y[7].startswith(m):
            N = ''
            for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
                N = N + str(x) + ', '
            MatrixArray[checklist.index(m)].append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
        else:
            pass

#when creating data, change 'a' in file attribute (last option) to 'w'; when appending, change 'w' to 'a'
#change the first argument in open(os.path.join()) to a folder you want to store the data in, and the second argument to the file name you want to write to.
print 'Sorting and saving ...'

for i in CalendarList:
    f = open(i + ' Movies.txt','a')
    for x in MatrixArray[CalendarList.index(i)]:
        f.write(x)
    f.close()

print 'Process finished.'

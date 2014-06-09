import requests
import os
from bs4 import BeautifulSoup
from boxofficemojo import retrieve_incomes
import string

path = r'C:\Users\Akshat Mahajan\Desktop\Scraper\Experimental-Screen-Scraping/Movie Data' #change file name to where you want your data to be saved.
os.chdir(path)

# The data returned by this code consists (in order) of movie name, lifetime gross, opening weekend box office revenue,
# and then the weekly box office revenue, stretching as long as BoxOfficeMojo holds the data.
print 'Initialising...'
L = []
M1 = []
M2 = []
M3 = []
M4 = []
M5 = []
M6 = []
M7 = []
M8 = []
M9 = []
M10 = []
M11 = []
M12 = []

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
    if y[7].startswith('1/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M1.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('2/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M2.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('3/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M3.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')   
    if y[7].startswith('4/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M4.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('5/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M5.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('6/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M6.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('7/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M7.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('8/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M8.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('9/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M9.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('10/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M10.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('11/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M11.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
    if y[7].startswith('5/'):
        N = ''
        for x in retrieve_incomes(findid(y[1]),full_week=False,use_cumes=False)['values']:
            N = N + str(x) + ', '
        M12.append(y[1] + ', ' + string.lower(y[3].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + string.lower(y[5].replace(' ','')).translate(string.maketrans("",""), string.punctuation)+', ' + N[:-1]+'\n')
#when creating data, change 'a' in file attribute (last option) to 'w'; when appending, change 'w' to 'a'
#change the first argument in open(os.path.join()) to a folder you want to store the data in, and the second argument to the file name you want to write to.
print 'Sorting and saving ...'
f = open('January Movies.txt','a')
for x in M1:
    f.write(x)
f.close()
f = open('February Movies.txt','a')
for x in M2:
    f.write(x)
f.close()
f = open('March Movies.txt','a') 
for x in M3:
    f.write(x)
f.close()
f = open('April Movies.txt','a') 
for x in M4:
    f.write(x)
f.close()
f = open('May Movies.txt','a')
for x in M5:
    f.write(x)
f.close()
f = open('June Movies.txt','a')
for x in M6:
    f.write(x)
f.close()
f = open('July Movies.txt','a')
for x in M7:
    f.write(x)
f.close()
f = open('August Movies.txt','a')
for x in M8:
    f.write(x)
f.close()
f = open('September Movies.txt','a')
for x in M9:
    f.write(x)
f.close()
f = open('October Movies.txt','a') 
for x in M10:
    f.write(x)
f.close()
f = open('November Movies.txt','a')
for x in M11:
    f.write(x)
f.close()
f = open('December Movies.txt','a') 
for x in M12:
    f.write(x)
f.close()
print 'Process finished.'

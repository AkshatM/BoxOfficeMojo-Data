import requests
import os
from bs4 import BeautifulSoup
from boxofficemojo import retrieve_incomes
import string
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
r = requests.get('http://www.boxofficemojo.com/genres/chart/?view=main&sort=gross&order=DESC&pagenum=1&id=scifiadventure.htm')
soup = BeautifulSoup(r.text)
#findid basically finds you the boxoffice movie id to plug into retrieve_incomes. It's written so that pesky 
#characters in brackets will be ignored.
#Apparently, this tactic will only cost us data about (500) Days of Summer and movies that end with year of 
#release in their titles, a small fraction of most movies.
def findid(n):
    if str(n).endswith(')'):
        m = str(n)[:str(n).find('(')]
        for link in soup.findAll('a', href=True, text=str(m)):
            return link['href'][12:-4]
    else:
        for link in soup.findAll('a', href=True, text=str(n)):
            return link['href'][12:-4]
for line in soup("tr"):
    L.append(line.get_text())
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
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'January Movies.csv'),'a')
for x in M1:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'February Movies.csv'),'a')
for x in M2:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'March Movies.csv'),'a') 
for x in M3:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'April Movies.csv'),'a') 
for x in M4:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'May Movies.csv'),'a')
for x in M5:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'June Movies.csv'),'a')
for x in M6:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'July Movies.csv'),'a')
for x in M7:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'August Movies.csv'),'a')
for x in M8:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'September Movies.csv'),'a')
for x in M9:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'October Movies.csv'),'a') 
for x in M10:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'November Movies.csv'),'a')
for x in M11:
    f.write(x)
f.close()
f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'December Movies.csv'),'a') 
for x in M12:
    f.write(x)
f.close()

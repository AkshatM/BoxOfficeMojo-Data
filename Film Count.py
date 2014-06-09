#this code will tell you how many films you have in your directory
import os
path = r'C:\Users\Akshat Mahajan\Desktop\Scraper\Experimental-Screen-Scraping\Movie Data'
L = 0
os.chdir(path)
for x in os.listdir(path):
    f = open(x),'r')
    for y in f:
        L+=1
    f.close()
print L

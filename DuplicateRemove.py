#use this code to eliminate duplicate entires that may have popped up while screen scraping
#remember to only use this one on file at a time
import os
path = r'C:\Users\Akshat Mahajan\Desktop\Scraper\Experimental-Screen-Scraping\Movie Data'
#change to location of stored data
os.chdir(path)
lines_seen = set() # holds lines already seen
outfile = open('December Movies 2.txt', "w") #recommend changing argument to simply 'name of file you'd like to run on' + 2, for convenience
for line in open('December Movies.txt', "r"): #change argument in 'open' to file you'd like to run this on
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

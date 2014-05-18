#use this code to eliminate duplicate entires that may have popped up while screen scraping
#remember to only use this one on file at a time
import os
lines_seen = set() # holds lines already seen
outfile = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'December Movies 2.txt'), "w")
for line in open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', 'December Movies.txt'), "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

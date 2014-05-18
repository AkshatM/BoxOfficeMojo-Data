#this code will tell you how many films you have in your directory
import os
L = 0
for x in os.listdir('C:/Users/Akshat Mahajan/Desktop/Movie Data'):
    f = open(os.path.join('C:/Users/Akshat Mahajan/Desktop/Movie Data', x),'r')
    for y in f:
        L+=1
    f.close()
print L-12

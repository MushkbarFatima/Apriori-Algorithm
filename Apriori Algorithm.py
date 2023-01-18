#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import csv
from collections import Counter


# In[20]:


#read txt file as csv
with open(r"M:\Lab assignment (unsupervised) material-20221130\movies.txt", newline='') as f:
    reader = csv.reader(f,delimiter=";")
    data = list(reader)                      #converting data into lists of lists

#Extracting unique movies
init = []
for i in data:
    for q in i:
      if(q not in init):
          init.append(q)
init = sorted(init)
print('Number of distinct movies: ',len(init))


# In[46]:


s=490

#make file for part a
with open(r"M:\Lab assignment (unsupervised) material-20221130\Assignment\oneItems.txt", 'w') as f:
 c = Counter()                
 for i in init:             # loop to print the frequency of distinct movies
     for d in data:
         if(i in d):
             c[i]+=1                  
 print("C1:")
 for i in c:
     one_item=str(c[i])+": "+ i   
     print(str([i])+": "+str(c[i]))
     f.write(one_item)
     f.write('\n')

 l = Counter()
 for i in c:
      if(c[i] >= 1):                          # loop to print the frequency of distinct movies again after abs min support  
         l[frozenset([i])]+=c[i]
 print("L1:")
 for i in l:
    print(str(list(i))+": "+str(l[i]))
 print()
 
 #make file for part b
 with open(r"M:\Lab assignment (unsupervised) material-20221130\Assignment\patterns.txt", 'w') as dc:
  pl = l
  pos = 1
  for count in range (2,15):
      nc = set()
      temp = list(l)
      for i in range(0,len(temp)):                           #loop to print the number of relationships between two(iter) movies
          for j in range(i+1,len(temp)):
              t = temp[i].union(temp[j])
              if(len(t) == count):
                  nc.add(temp[i].union(temp[j]))
      nc = list(nc)
      c = Counter()
      for i in nc:
          c[i] = 0
          for q in data:
             temp = set(q)
             if(i.issubset(temp)):
                 c[i]+=1
      print("C"+str(count)+":")
      for i in c:
          print(str(list(i))+": "+str(c[i]))
      print()
      l = Counter()
      for i in c:
           if(c[i] >= s):
              l[i]+=c[i]
      print("L"+str(count)+":")
      for i in l:
          print(str(list(i))+": "+str(l[i]))  
          one_item2=str(l[i])+": "+str(list(i))
          dc.write(one_item2)
          dc.write('\n')

      print()
      if(len(l) == 0):
          break
      pl = l
      pos = count
  print("Result: ")
  print("L"+str(pos)+":")
  for i in pl:                        #loop to print the movies having freq itemset
     print(str(list(i))+": "+str(pl[i]))
  print()


import csv
import math
import collections
from collections import Counter

def EntFunc(list):
    j=0
    Entropy = 0
    for j in range(0,len(BusinessName)):
        if BusinessName[j] != BusinessName[j-1]:
            p = float(BusinessName.count(BusinessName[j]))/float(len(BusinessName))
            Entropy = -1.0*math.log(p)*p + Entropy
            print j,BusinessName[j],BusinessName.count(BusinessName[j]),p
        j=j+1
    print Entropy

ReadFile = 'SIC581208.csv'
inf = csv.reader(open(ReadFile,"rU"))
i = 0
j = 0
BusinessName = []
for row in inf:
    i = 1+1
    if i > 1:
        zip = row[6]
        if zip == '90002':
            name = row[1]
            BusinessName.append(name)
            j=j+1
print Counter(BusinessName)
print set(BusinessName)

EntFunc(BusinessName)

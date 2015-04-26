import csv
import math
import collections
from collections import Counter

# EntFunc calculates the Shannon index for the diversity of venues in a given zip code.
def EntFunc(list,list2):
    k = 0
    Entropy = 0
    for k in range(0, len(BusinessName)):
        if BusinessName[k] != BusinessName[k - 1]:
            p = float(BusinessName.count(BusinessName[k])) / float(len(BusinessName))
            Entropy = -1.0 * math.log(p) * p + Entropy
        k = k + 1
    if Entropy != 0:
        NormalizedEntropy=Entropy/math.log(k)
        data=zip[j],k,Entropy,NormalizedEntropy
        print data
        wr.writerow(data)

#Take in data from ESRI business lists by zip code.
#The entry matrix takes in values by zip code then the business name within the zip code.
#The BusinessName list is there simply to take in business names and determine how often unique values repeat for diversity calculations.
FilePrefix='SIC5813'
ReadFile = '{FilePrefix}.csv'.format(FilePrefix=FilePrefix)
inf = csv.reader(open(ReadFile, "rU"))
i = 0
entry=[[],[]]
BusinessName=[]

#Store zip and business name data from ESRI file.
for row in inf:
    i = i + 1
    if i > 1:
        entry[0].append(long(row[6]))
        entry[1].append(row[1])

#Sort the zip code values by zip code.
zip = sorted(list(set(entry[0])),key=float)

#Sort all stored information by zip code.
#Output business diversity by zip code.
j=0
entry.sort(key=lambda x: x[0])
WriteFile='{FilePrefix}output.csv'.format(FilePrefix=FilePrefix)
fileWriter = open(WriteFile,'wb')
wr = csv.writer(fileWriter)
label=["Zip code","Number of businesses","Shannon index of businesses in zip code","Normalized entropy"]
wr.writerow(label)
for i in range(0,len(entry[0])):
    if entry[0][i] == zip[j]:
        BusinessName.append(entry[1][i])
    else:
        EntFunc(BusinessName,zip[j])
        j=j+1
        BusinessName=[]

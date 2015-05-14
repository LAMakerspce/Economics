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
FilePrefix='SIC5812'
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

#Read in food desert data which contains both zip and ZCTA values.
zipfile = 'CAFoodDesertZip.csv'
zipreader = csv.reader(open(zipfile, "rU"))
i=0
zipentry = [[],[],[],[],[]]
for row in zipreader:
    i=i+1
    if i>1:
        zipentry[0].append(long(row[0]))
        zipentry[1].append(long(row[1]))
        zipentry[2].append(int(row[2]))
        zipentry[3].append(int(row[3]))
        zipentry[4].append(int(row[4]))

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
fileWriter.close()

ReadFile2='{FilePrefix}output.csv'.format(FilePrefix=FilePrefix)
inf2 = csv.reader(open(ReadFile2, "rU"))
i=0
entropyentry = [[],[],[],[]]
for row in inf2:
    i=i+1
    if i>1:
        entropyentry[0].append(long(row[0]))
        entropyentry[1].append(int(row[1]))
        entropyentry[2].append(float(row[2]))
        entropyentry[3].append(float(row[3]))

WriteFile2='{FilePrefix}ZipAndEntropy.csv'.format(FilePrefix=FilePrefix)
fileWriter2=open(WriteFile2,'wb')
wr2 = csv.writer(fileWriter2)
label=["Zip code","ZCTA","Number of businesses in zip code","Shannon index of businesses in zip code","Normalized entropy","LILATracts_1And10: Low income and low access measured at 1 and 10 miles","LILATracts_halfAnd10: Low income and low access measured at 1/2 and 10 miles","LILATracts_1And20: Low income and low access measured at 1 and 20 miles"]
wr2.writerow(label)
for i in range(0,len(entropyentry[0])):
    match = sorted([x for x,val in enumerate(zipentry[0]) if val == entropyentry[0][i]])
    for j in range(0,len(match)):
        data2 = zipentry[0][match[j]],zipentry[1][match[j]],entropyentry[1][i],entropyentry[2][i],entropyentry[3][i],zipentry[2][match[j]],zipentry[3][match[j]],zipentry[4][match[j]]
        print data2
        wr2.writerow(data2)

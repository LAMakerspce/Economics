import csv
import math

inf = csv.reader(open('2008dataFormatted.csv',"rU"))
# Data file containing Bureau of Labor Statistics

fileWriter = open('JobEntropy2008.csv','wb')
wr = csv.writer(fileWriter)
label = ["State","Job entropy"]
wr.writerow(label)

i = 0

stateNum = 1
stateName = []
entropy = 0
# Entropy is the Shannon entropy of job roles by state
index = 0

# These lists are used to store the name and order of states as the Shannon index is looped through by state.
for row in inf:
	i = i+1
	if row[8] == "**": row[8] = 1
	if i > 1:
		if stateNum == int(row[0]):
#The modulo statement filters out redundant entries
			if int(row[3])%10000 > 0: entropy = entropy - float(row[8])*(math.log(float(row[8]))/math.log(2.718281828))
			stateName.append(row[2])
			index = index+1
#Output entropy per state/territory
		if stateNum != int(row[0]):
			print stateName[index-1],entropy
			data = stateName[index-1],entropy
			wr.writerow(data)
			stateNum = int(row[0])
			entropy = 0
#This captures the last state/territory in the file
else:
	print row[2],entropy
	data = row[2],entropy
	wr.writerow(data)

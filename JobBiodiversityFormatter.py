import csv
import math

inf = csv.reader(open('2008data.csv',"rU"))
# Data file containing Bureau of Labor Statistics

fileWriter = open('2008dataFormatted.csv','wb')
wr = csv.writer(fileWriter)
label = ["AREA", "ST", "STATE", "OCC_CODE", "OCC_TITLE", "OCC_GROUP", "TOT_EMP","EMP_PRSE","JOBS_1000"]
wr.writerow(label)

i = 0
j = 1
k = 0
employmentPerMil = 0
# employmentPerMil is the fraction of jobs per 1000.

for row in inf:
	i = i+1
	if row[6] == "**":
		row[6] = 0
	if row[7] == "**":
		row[7] = 0

# This filters out junk values for the fraction of total employment per job type.

	if i > 1:
		titleNum = int(row[3])
		if titleNum == 0:
			employmentTotal = float(row[6])
			
		else:
			employmentPerMil = float(row[6])/employmentTotal
		if employmentPerMil == 0:
			employmentPerMil = 1
		print employmentPerMil
		data = row[0],row[1],row[2],row[3],row[4],row[5],row[6], row[7],employmentPerMil
		wr.writerow(data)

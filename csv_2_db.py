import csv

file1 = open('clean_measure.csv')

print(type(file1))


csvreader = csv.reader(file1)

header = []
header = next(csvreader)


print("super")

rows = []
for row in csvreader:
        rows.append(row)


file1.close()
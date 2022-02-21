import csv
with open("sample.csv", 'r+' ,newline='') as csvfile:
    for row in csv.reader(csvfile):
        row.append('new element')
        print(', '.join(row))

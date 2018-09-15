import csv
with open('example1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if (int(row[1])>>30):
            hike=int(row[2])+(int(row[2])*0.2)
            print(row[0],row[1],hike,row[3])
        else:
            print(row[0],row[1],row[2],row[3])
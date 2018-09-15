
import csv
with open("/home/hunter/PycharmProjects/python-class/testcsv.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    n=int(input("enter the line number"))
    rn = 1

    for row in readCSV:
        if(rn==n):
            print(row[0],row[1],row[2],row[3])
        rn=rn+1
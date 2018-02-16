import csv

csvfile = open("ex.csv", "r")
reader = csv.reader(csvfile)

resultlist = []

outfile=open("edgelist.csv", "w")
writer=csv.writer(outfile)
for row in reader:
    for person in row:
        myindex = row.index(person)
        newlist = row[:myindex]+row[myindex+1:]   #make a new temp list without the person in it
        for item in newlist:
            mytuple = (person, item)
            backtuple = (item, person)
            if backtuple not in resultlist: #remove any reversed duplicates
                resultlist.append(mytuple)
                writer.writerow(mytuple)

csvfile.close()
outfile.close()
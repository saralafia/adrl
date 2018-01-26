import csv
import time

#import tab-delimited keywords file
f = open('gazetteers/us-places-clean.txt','r')
#gazetteer = f.read().lower().split("\r")
citylist = f.read().strip().split("\r")
f.close()
print(citylist[0:5])

gazetteer = []

for word in citylist:
    word = word.rstrip()
    gazetteer.append(word)

print(gazetteer[0:10])

theses = []
fullRow = []
with open('adrl.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #the full row for each entry, which will be used to recreate the improved CSV file in a moment
        fullRow.append((row['key'], row['title'], row['description']))

        #the column we want to parse for our keywords
        #row = row['description'].lower()
        row = row['description']
        theses.append(row)

#NEW! a flag used to keep track of which row is being printed to the CSV file
counter = 0

#NEW! use the current date and time to create a unique output filename
timestr = time.strftime("%Y-%m-%d-(%H-%M-%S)")
filename = 'output-' + str(timestr) + '.csv'

#NEW! Open the new output CSV file to append ('a') rows one at a time.
with open(filename, 'a') as csvfile:

    #NEW! define the column headers and write them to the new file
    fieldnames = ['key', 'title', 'description', 'place']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    #NEW! define the output for each row and then print to the output csv file
    writer = csv.writer(csvfile)

    #OLD! this is the same as before, for currentRow in fullRow:
    # for texts in allTexts:

    for thesis in theses:
        matches = 0
        storedMatches = []

        #for each entry:
        #allWords = entry.split(' ')
        #for words in texts:

            #remove punctuation that will interfere with matching
            # words = words.replace(',', '')
            # words = words.replace('.', '')
            # words = words.replace(';', '')

            #if a keyword match is found, store the result.
        for place in gazetteer:
            if place in thesis:
                if place in storedMatches:
                    continue
                else:
                    storedMatches.append(place)
                    # print(place)
                matches += 1

        #CHANGED! send any matches to a new row of the csv file.
        if matches == 0:
            newRow = fullRow[counter]
        else:
            matchTuple = tuple(storedMatches)
            newRow = fullRow[counter] + matchTuple

        #NEW! write the result of each row to the csv file
        writer.writerows([newRow])
        counter += 1
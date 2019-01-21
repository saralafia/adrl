from ..shp import databasefile

def normalize(inName,outName,start,end,direction,minEqMax,fieldNames,decimalPlaces):
    inTable=databasefile.DatabaseFile([],[],[],inName)
    fieldIndicies=[]
    minEqMax=str(minEqMax)
    if len(fieldNames)==0:
        for id,f in enumerate(inTable.fieldspecs):
            if f[0]=="N":
                fieldIndicies.append(id)
    else:
        for f in fieldNames:
            fieldIndicies.append(inTable.index(f))

    outTable=databasefile.DatabaseFile(map(inTable.fieldnames.__getitem__,fieldIndicies),
                                       map(inTable.fieldspecs.__getitem__,fieldIndicies),
                                       [map(float,map(row.__getitem__,fieldIndicies)) for row in inTable])


    if direction=="column":
        minimums=map(float,outTable.records[0])
        maximums=map(float,outTable.records[0])
        for row in outTable:
            for id,n in enumerate(row):
                if n < minimums[id]:
                    minimums[id]=n
                elif n > maximums[id]:
                    maximums[id]=n
        for rowID,row in enumerate(outTable.records):
            for id,n in enumerate(row):
                try:
                    outTable.records[rowID][id]=str(round(start+((end-start)*(n-minimums[id])/float(maximums[id]-minimums[id])),decimalPlaces))
                    outTable.records[rowID][id]=outTable.records[rowID][id][:outTable.records[rowID][id].rfind(".")+1+decimalPlaces]
                except ZeroDivisionError:
                    outTable.records[rowID][id]=minEqMax
    elif direction=="global":
        minimum=min(map(min,outTable.records))
        maximum=max(map(max,outTable.records))
        for rowID,row in enumerate(outTable.records):
            for id,n in enumerate(row):
                try:
                    outTable.records[rowID][id]=str(round(start+((end-start)*(n-minimum)/float(maximum-minimum)),decimalPlaces))
                    outTable.records[rowID][id]=outTable.records[rowID][id][:outTable.records[rowID][id].rfind(".")+1+decimalPlaces]
                except ZeroDivisionError:
                    outTable.records[rowID][id]=minEqMax

    elif (direction=="row"):
        for id,row in enumerate(outTable.records):
            minimum=min(row)
            maximum=max(row)
            values=[]
            for n in row:
                try:
                    values.append(str(round(start+((end-start)*(n-minimum)/float(maximum-minimum)),decimalPlaces)))
                except ZeroDivisionError:
                    values.append(str(minEqMa))
            outTable.records[id]=values

    for rowId,row in enumerate(outTable):
        for columnId,value in enumerate(row):
            inTable[rowId][fieldIndicies[columnId]]=value

    outTable.dynamicSpecs()
    for id, spec in enumerate(outTable.fieldspecs):
        inTable.fieldspecs[fieldIndicies[id]]=spec

    inTable.writeFile(outName)        
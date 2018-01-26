from geotext import GeoText


iterate_descriptions_titles = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/titles_descriptions.txt', 'r')
descriptions_titles = iterate_descriptions_titles.readlines()
iterate_descriptions_titles.close()
place_names = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/place_names.txt', 'w')
n = 0

for line in descriptions_titles:  
    t = GeoText(line).cities
    n += 1
    print n
    count_sf = t.count("San Francisco")
    count_sb = t.count("Santa Barbara")
    count_la = t.count("Los Angeles")
    print "San Francisco: " + str(count_sf)
    print "Santa Barbara: " + str(count_sb)
    print "Los Angeles: " + str(count_la)
    place_names.write(str(count_sf) + "\t" + str(count_sb) + "\t" + str(count_la) + "\n")

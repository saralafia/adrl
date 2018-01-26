import tf_idf_giuz

# In this scirpt only the paths have to be changed, if necessary. Additionally, the amount of clusters have to be adapted, if necessary. 
# additionally, the "STOPWORD_PERCENTAGE_THRESHOLD = 1.2" value can be adapted, if the script should use the self-created stopword list (under def save_corpus_to_file). 
# the following two lines have to be adapted for each cluster
#     keywords = my_tfidf.get_doc_keywords(input_lines_prep_18)
#     output_file_cluster = open('C:/Users/abruggma/Documents/_PhD/Sonstiges/Oli/tfidf/kmeans_output/k_means_tfidf_cl18.txt', 'w')
 

input_file_prep_01 = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/Corpus/all_but_SF_SB_LA.txt', 'r')
input_lines_prep_01 = input_file_prep_01.read()
input_file_prep_02 = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/Corpus/Los_Angeles.txt', 'r')
input_lines_prep_02 = input_file_prep_02.read()
input_file_prep_03 = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/Corpus/San_Francisco.txt', 'r')
input_lines_prep_03 = input_file_prep_03.read()
input_file_prep_04 = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/Corpus/Santa_Barbara.txt', 'r')
input_lines_prep_04 = input_file_prep_04.read()


input_file_prep_01.close()
input_file_prep_02.close()
input_file_prep_03.close()
input_file_prep_04.close()


my_tfidf = tf_idf_giuz.TfIdf()
##keywords = my_tfidf.get_doc_keywords("the spoon and the fork")
my_tfidf.add_input_document(input_lines_prep_01)
my_tfidf.add_input_document(input_lines_prep_02)
my_tfidf.add_input_document(input_lines_prep_03)
my_tfidf.add_input_document(input_lines_prep_04)


#print ("Input doc: " + str(input_doc))
my_tfidf.save_corpus_to_file('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/Corpus/filename.txt', 'C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/Corpus/stopwords.txt',
                          STOPWORD_PERCENTAGE_THRESHOLD = 1.2)

##Bedeutung Stopword_Percentage_Threshold -> in wievielen Dokumenten kommt Wort vor < eingesetzter Wert * gesamte Anzahl Dokumente -> falls erfuellt, wird nicht in Stoppwortliste aufgenommen

num_docs = my_tfidf.get_num_docs()
print ("Number of docs: " + str(num_docs))
#single_idf = my_tfidf.get_idf("c")
#print ("idf of c: " + str(single_idf))

keywords = my_tfidf.get_doc_keywords(input_lines_prep_04)
#print (keywords)

output_file_cluster = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/Corpus/tfidf_04_Santa_Barbara.txt', 'w')

print ("Write tf-idf list...")

for item in keywords:
    print>>output_file_cluster, item

output_file_cluster.close()    

print ("Script successfully executed.")
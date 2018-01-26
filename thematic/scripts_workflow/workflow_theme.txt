Run the "website_to_text_2.py" script (Python 2.7!)


Run the "htmlparser_ucsb.py" script (Python 3!)


Copy & paste the output of the "htmlparser_ucsb.py" into an Excel table. Arrange the Excel table as follows: 1. column: identifier (i.e., pid), 2. column: label (i.e., pid), 3. column: title, 4. column description


Copy & paste the Excel table contents into a text editor. Substitute all "\t" by a " ," and save the file as a .txt file. 


Creating MALLET file (be sure not to include the last document which is not a dissertation!)

C:\mallet>bin\mallet import-file --input c:\mallet\data_ucsb\adrl.txt --output data_ucsb\adrl_stopwords_remove.mallet --keep-sequence --stoplist-file c:\mallet\stoplists\en.txt


Command line prompt for testing the model fit of different TM solutions (i.e., different numbers of topics)

bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 1 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 2 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 3 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 4 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 5 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 6 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 7 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 8 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 9 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 10 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
...
...
...


Run "extract_log_likelihood.py" script to extract the LLT values. Decide for a TM solution with a low LLT value. 


Command Line Prompt for a specific TM solution

C:\mallet>bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 71 --optimize-interval 10 --output-doc-topics C:\mallet\data_ucsb\adrl_hyper_par_ll_t71_output_topics.txt 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll_t71.txt


Running SOM Analyst with the following parameteres

x / y dimensions: 42x42 (i.e., 1764 hexagons)
lenght of training: 50,000 / 500,000
initial neighborhood radius: 42 / 6


Run "geotext.py" script in order to extract San Francisco, Santa Barbara, and Los Angeles place names from a text file (descriptions and titles, one line for each thesis)


Run "tfidf_adrl.py" (tf_idf_giuz.py has to be in the same folder) in order to extract most relevant terms for theses about the selected locations (i.e., San Francisco, Santa Barbara, and Los Angeles)


To do

- decide how many topics to create
- stemming texts (e.g., with TreeTagger, see here: http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)
- exclude non-english dissertations from text analysis
- decide for years dissertations have been published to be included
- remove stopwords (spatial/temporal data?)

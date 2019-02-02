## Preprocessing
### Harvesting metadata
Run the **"website\_to\_text_2.py"** script (in Python 2.7) and run the **"htmlparser\_ucsb.py"** script (in Python 3). Copy and paste the output of the **"htmlparser\_ucsb.py"** into an Excel table. Arrange the Excel table as follows: 1. column: identifier (i.e., pid), 2. column: label (i.e., pid), 3. column: title, 4. column description. Copy and paste the Excel table contents into a text editor. Substitute all "\t" by a " ," and save the file (**"adrl\_raw.csv"**).

### Modelling topics
To create the MALLET file, run C:\mallet>bin\mallet import-file --input c:\mallet\data_ucsb\adrl.txt --output data_ucsb\adrl_stopwords_remove.mallet --keep-sequence --stoplist-file c:\mallet\stoplists\en.txt

Next, use the following command line prompt for testing the model fit of different topic model solutions (i.e. to try different numbers of topics):

bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 1 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt  & 
bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 2 --optimize-interval 10 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll.txt
...
...
...


Run "extract_log_likelihood.py" script to extract the LLT values. Decide for a TM solution with a low LLT value. Then, use the following command Line Prompt to   solve for a specific topic model solution (in this case, 71 topics):

C:\mallet>bin\mallet train-topics --input C:\mallet\data_ucsb\adrl_stopwords_remove.mallet --num-topics 71 --optimize-interval 10 --output-doc-topics C:\mallet\data_ucsb\adrl_hyper_par_ll_t71_output_topics.txt 2>> C:\mallet\data_ucsb\adrl_hyper_par_ll_t71.txt

Save topic list (**"adrl\_topiclist.csv"**) and output (**"adrl\_thesis\_topics.csv"**).
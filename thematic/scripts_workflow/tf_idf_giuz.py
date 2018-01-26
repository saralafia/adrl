#!/usr/bin/env python
# 
# Copyright 2010  Niniane Wang (niniane@gmail.com)
# Reviewed by Alex Mendes da Costa.
# 
# This is a simple Tf-idf library.  The algorithm is described in
#   http://en.wikipedia.org/wiki/Tf-idf
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__author__ = "Niniane Wang"
__email__ = "niniane at gmail dot com"



# in this script, only this line of code has to be adapted for the external stopword list: stopwords_manual = open('C:/Users/abruggma/Documents/_PhD/Sonstiges/Oli/tfidf/kmeans_output/stopword_nltk.txt', 'r')




# in this script 

import math
import re
from operator import itemgetter

class TfIdf:

  """Tf-idf class implementing http://en.wikipedia.org/wiki/Tf-idf.
  
     The library constructs an IDF corpus and stopword list either from
     documents specified by the client, or by reading from input files.  It
     computes IDF for a specified term based on the corpus, or generates
     keywords ordered by tf-idf for a specified document.
  """

  def __init__(self, corpus_filename = None, stopword_filename = None,
               DEFAULT_IDF = 1.5):
    """Initialize the idf dictionary.  
    
       If a corpus file is supplied, reads the idf dictionary from it, in the
       format of:
         # of total documents
         term: # of documents containing the term

       If a stopword file is specified, reads the stopword list from it, in
       the format of one stopword per line.

       The DEFAULT_IDF value is returned when a query term is not found in the
       idf corpus.
    """
    print("_init_ started...")
    print("Input corpus: " + str(corpus_filename))
    print("Input stopword list: " + str(stopword_filename))
    self.num_docs = 0
    self.term_num_docs = {}     # term : num_docs_containing_term
    self.stopwords = []
    self.idf_default = DEFAULT_IDF

    if corpus_filename:
      corpus_file = open(corpus_filename, "r")

      # Load number of documents.
      line = corpus_file.readline()
      self.num_docs = int(line.strip())

      # Reads "term:frequency" from each subsequent line in the file.
      for line in corpus_file:
        tokens = line.rpartition(":")
        term = tokens[0].strip()
        frequency = int(tokens[2].strip())
        self.term_num_docs[term] = frequency
        #print(term)

    if stopword_filename:
      stopword_file = open(stopword_filename, "r")
      self.stopwords = [line.strip() for line in stopword_file]
      #print('\n' + "stopword: "+ line)
      

  def get_tokens(self, str):
    """Break a string into tokens, preserving URL tags as an entire token.

       This implementation does not preserve case.  
       Clients may wish to override this behavior with their own tokenization.
    """
    return re.findall(r"<a.*?/a>|<[^\>]*>|[\w'@#]+", str.lower())

  def add_input_document(self, input):
    """Add terms in the specified document to the idf dictionary."""
    """However, we already have a dictionary specified in the example!"""
    print("Add input document...")
    self.num_docs += 1
    words = set(self.get_tokens(input))
    #print(words)    
    for word in words:
      if word in self.term_num_docs:
        self.term_num_docs[word] += 1
      else:
        self.term_num_docs[word] = 1

  def save_corpus_to_file(self, idf_filename, stopword_filename,
                          STOPWORD_PERCENTAGE_THRESHOLD = 0.01):
    """Save the idf dictionary and stopword list to the specified file."""
    output_file = open(idf_filename, "w")

    output_file.write(str(self.num_docs) + "\n")
    for term, num_docs in self.term_num_docs.items():
      output_file.write(term + ": " + str(num_docs) + "\n")

    sorted_terms = sorted(self.term_num_docs.items(), key=itemgetter(1),
                          reverse=True)
    #print(sorted_terms)
    #print(num_docs)
    #print(self.num_docs)
    stopword_file = open(stopword_filename, "w")
    for term, num_docs in sorted_terms:
      if num_docs < STOPWORD_PERCENTAGE_THRESHOLD * self.num_docs:
        break

      stopword_file.write(term + "\n")
      #print("Term input stopwordlist: " + term)

  def get_num_docs(self):
    """Return the total number of documents in the IDF corpus."""
    return self.num_docs

  def get_idf(self, term):
    """Retrieve the IDF for the specified term. 
    
       This is computed by taking the logarithm of ( 
       (number of documents in corpus) divided by (number of documents
        containing this term) ).
     """
    #print ("Hello from get_idf")
    ##print("Stoppwoerter" + str(self.stopwords))
    
    stopwords_manual = open('C:/Users/abruggma/Documents/_PhD/GIUZ_Viz/tfidf/Stopwords/stopword_nltk.txt', 'r')
    stopwords_manual_01 = stopwords_manual.read()
    
    #print ("Stopwords_manual_01: " + stopwords_manual_01)
   
    # direkt untenstehende Variante ist die Originale, 2 Linien unten ist die Variante, eine eigene, externe Liste zu beruecksichtigen
    #if term in self.stopwords:
    if term in stopwords_manual_01:
      #print ("Term in stopwordlist: " + str(term))
      return 0

    if not term in self.term_num_docs:      
      return self.idf_default
      #print ("self.idf_default: " + self.idf_default)
    
    #print(term)
    #print(float(1+self.get_num_docs()))
    #print(1 + self.term_num_docs[term])
    
    #return math.log(float(1 + self.get_num_docs()) / 
    #  (1 + self.term_num_docs[term]), 10)
    
    return math.log(1 + (float(self.get_num_docs()) / 
      (self.term_num_docs[term])), 10)
    
    
    ## ob Logarithmus mit Basis 10 oder e ist egal gemaess Wikipedia
    ## Achtung: Mit der Original-Formel (oben math.log(float(1 + self.get...) werde alle Woerter ausgeschlossen, welche mindestens einmal in allen Texten vorkommen (da log10 (1/1) = 0)
    ## Moeglichkeit: 1 + (N/gft) anstelle von (N+1)/(gft+1)
    

  def get_doc_keywords(self, curr_doc):
    """Retrieve terms and corresponding tf-idf for the specified document.

       The returned terms are ordered by decreasing tf-idf.
    """
    print("Get_doc_keywords running...")
    tfidf = {}
    tokens = self.get_tokens(curr_doc)
    #print("Tokens: " + str(tokens))
    tokens_set = set(tokens)
    for word in tokens_set:
      # The definition of TF specifies the denominator as the count of terms
      # within the document, but for short documents, I've found heuristically
      # that sometimes len(tokens_set) yields more intuitive results.
      mytf = float(tokens.count(word)) / len(tokens)
      myidf = self.get_idf(word)
      #print (word)
      #print ("myidf: " + str(self.get_idf(word)))
      tfidf[word] = mytf * myidf
      
      # In Original umgesetzte Formel -> Haeufigkeit Wort in Dokument / Anzahl Worte in Dokument * loge ((Anzahl Dokumente + 1) / (Anzahl Dokumente, in denen Wort mindestens 1 mal vorkommt + 1)) 

    return sorted(tfidf.items(), key=itemgetter(1), reverse=True)


##my_tfidf = TfIdf("C:/Users/abruggma/Documents/_PhD/Software/tf-idf/tfidf/tfidf/tfidf_testcorpus.txt", "C:/Users/abruggma/Documents/_PhD/Software/tf-idf/tfidf/tfidf/tfidf_teststopwords.txt",
##                           DEFAULT_IDF = 1.5)

##my_tfidf.get_doc_keywords("C:/Users/abruggma/Documents/_PhD/Software/tf-idf/tfidf/tfidf/tfidf_testcorpus.txt")


##input_document = "C:/Users/abruggma/Documents/_PhD/Software/tf-idf/tfidf/tfidf/tfidf_testcorpus.txt"

##TfIdf.add_input_document()



##print (my_tfidf)


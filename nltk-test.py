from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

# st = StanfordNERTagger('/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz','/usr/share/stanford-ner/stanford-ner.jar',encoding='utf-8')

descriptions = open("/Users/saralafia/Downloads/stanford-ner-2017-06-09/descriptions.txt").read()
split_descriptions = descriptions.split()

# changed path according to system - classifier currently in DOWNLOADS folder
classifier = '/Users/saralafia/Downloads/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz'
ner_path = '/Users/saralafia/Downloads/stanford-ner-2017-06-09/stanford-ner.jar'

st = StanfordNERTagger(classifier,ner_path,encoding='utf-8')
#text = "The topic of this dissertation is Guca, a dialect of Kwak' wala, an endangered Wakashan language that is spoken on the northern end of Vancouver Island, British Columbia and the adjacent mainland. This study is based on a corpus of elicited and naturalistic language recordings made in the home of the Wallas family of Quatsino between 2011 and 2014. The study contributes to the documentation of this little-studied dialect by describing, in Chapter 2, the phoneme inventory and the phonetic character of the segments as well as common phonological processes in this variety of the language. In addition, the phonotactics of the language are documented and investigated with regards to their potential phonetic bases in Chapter 3. The typologically unusual lexical stress system displays"
pure_tokens = split_descriptions[::2]

#tokenized_text = word_tokenize(text)
tokenized_text = word_tokenize(pure_tokens)
classified_text = st.tag(tokenized_text)
#print(classified_text)
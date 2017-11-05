# NLP Resources
https://radimrehurek.com/gensim/models/word2vec.html
https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/
https://nlp.stanford.edu/software/tagger.shtml # jar for pos tagger

#Commands POS tag

java -cp ../POS/stanford-postagger-full-2015-04-20/stanford-postagger.jar  edu.stanford.nlp.tagger.maxent.MaxentTagger -model ../POS/stanford-postagger-full-2015-04-20/models/english-left3words-distsim.tagger -textFile  A00-1001.txt


#Data Parsing
run parser.AuthorPaperText.py to generate author files with all papers data appended in one file
run utils.nlp_parser.py.write_author_noun_phrases() to generate author files with all topics(noun phrases) data separated by comma in one file

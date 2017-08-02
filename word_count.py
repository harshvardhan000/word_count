
import pprint
import time
from nltk.corpus import reuters

start_data_prep = time.time()
################################Data Preparation and data preprocessing############################################

documents = reuters.fileids()

#Collecting total words in all documets in all categories
doc_words = reuters.words(documents)

#creating a unique set of words(for which we have to apply word count) from the collection of total words found in all documents.
doc_set   = set(doc_words)
            
doc_list  =  list(doc_set)             
doc_cor_list = []

#As the words are encoded so removing the ascii format
for word in doc_list:
    doc_cor_list.append(word.encode('ascii','ignore'))

doc_cor_upper_list = []

#Converting the words to upper format
for word in doc_cor_list:              
	doc_cor_upper_list.append(word.upper())



book_words=[]

#Storing the words in plot.list and preprocessing the dataset
with open('plot.list','r') as f:
	for line in f:
	    for word in line.split():

#If the token contains non-alphanumeric character such as punctuation(leading or trailing),trimming it off here
		if not word.isalnum() and (not word[0].isalnum() or not word[-1].isalnum()):
				
			while len(word) > 0 and not word[0].isalnum():
	    			word = word[1:]
		
			while len(word) > 0 and not word[-1].isalnum():
	    			word = word[:-1]
 			
			
# Checking the token is alphanumeric but does not contain digit (remove cases such as '195-264', '23')

		if word.isalnum() and not word.isdigit():
		        book_words.append(word.upper())

end_data_prep = time.time()

##########################word_count calculation######################################################
start_word_count = time.time()

dict_upper_list = {}

#Creating a dictionary for the words for we need to compute word count in plot.list
for word in doc_cor_upper_list:
        dict_upper_list[word]=0


for word in book_words:
	if dict_upper_list.has_key(word):
		dict_upper_list[word] = dict_upper_list[word] + 1

end_word_count = time.time()

pprint.pprint(dict_upper_list)



print "Data preparation and data processing time is " + str(end_data_prep - start_data_prep)

print "word_count_computation time is " + str(end_word_count - start_word_count)

 












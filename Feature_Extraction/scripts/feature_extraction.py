import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import numpy as np
import pandas 
from os import listdir
from os.path import isfile, join
import csv 



####################################################
#Get names of all files in /Data/raw_data directory 
####################################################
def get_files():
	onlyfiles = [f for f in listdir("../../Data/raw_data/formatted_data/") if isfile(join("../../Data/raw_data/formatted_data/", f))]
	return onlyfiles


#####################################################################
#Generate top 100 trigrams for all files in /Data/raw_data.
#Output results to:
#	 /Feature_Extraction/trigram_data/trigram_<original_filename>.csv
#####################################################################
def trigram_generator(onlyfiles):	
	for file_name in onlyfiles:
		df = pandas.read_csv("../../Data/raw_data/formatted_data/" + file_name,dtype={'BODY':str})
		corpus = []
		output = []
		for row in df['BODY'].str.split():
			trigram = []
			if type(row) == float:
				continue
			trigram = nltk.ngrams(row,3)
			for grams in trigram:
				corpus.append(grams)

		fdist = nltk.FreqDist(corpus)

		for gram, freq in fdist.most_common(100):
			output.append(gram)

		create_file = "../trigram_data/trigram_"+file_name 
		with open(create_file,'wb') as myfile:
			myfile.write('\n'.join('%s_%s_%s' % x for x in output))

#####################################################################
#Generate top 100 bigrams for all files in /Data/raw_data.
#Output results to:
#	 /Feature_Extraction/bigram_data/bigram_<original_filename>.csv
#####################################################################
def bigram_generator(onlyfiles):
#	stops = set(stopwords.words('english'))

	for file_name in onlyfiles:
		df = pandas.read_csv("../../Data/raw_data/formatted_data/" + file_name,dtype={'BODY':str})
		bigram = []
		output = []
	
		for row in df['BODY']:
			line = []
			if type(row) == float:
				continue 	
			for word in row.split():
				#tagged = nltk.word_tokenize(word)
				#tagged_sent = nltk.pos_tag(tagged)
				#word,pos = tagged_sent[0]
				#if word not in stops and pos != 'NNP':
				#if pos != 'NNP':
				line.append(word)
				bigram += nltk.bigrams(line)


		fdist = nltk.FreqDist(bigram)

		for gram, freq in fdist.most_common(100):
			output.append(gram)
			
		create_file = "../bigram_data/bigram_"+file_name 
		with open(create_file,'wb') as myfile:
			myfile.write('\n'.join('%s_%s' % x for x in output))


def unigram_generator(onlyfiles):	

	for file_name in onlyfiles:
		df = pandas.read_csv("../../Data/raw_data/formatted_data/" + file_name,dtype={'BODY':str})
		corpus = []
		output = []
		for row in df['BODY'].str.split():
			if type(row) == float:
				continue
			for word in row:
				corpus.append(word)

		fdist = nltk.FreqDist(corpus)
		mc = fdist.most_common(100)

		for gram, freq in mc:
			output.append(gram)

		create_file = "../unigram_data/unigram_"+file_name 
		with open(create_file,'wb') as myfile:
			myfile.write('\n'.join(output))


if __name__ == "__main__":
	f = get_files()
	unigram_generator(f)
	bigram_generator(f)
	trigram_generator(f)

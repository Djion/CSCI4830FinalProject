import nltk
import numpy as np
import pandas 
from os import listdir
from os.path import isfile, join
import csv 

####################################################
#Get names of all files in /Data/raw_data directory 
####################################################
def get_files():
	onlyfiles = [f for f in listdir("../../Data/raw_data/") if isfile(join("../../Data/raw_data/", f))]
	return onlyfiles

#####################################################################
#Generate top 100 bigrams for all files in /Data/raw_data.
#Output results to:
#	 /Feature_Extraction/bigram_data/bigram_<original_filename>.csv
#####################################################################
def bigram_generator(onlyfiles):
	for file_name in onlyfiles:
		output = []
		bigram = []

		df = pandas.read_csv("../../Data/raw_data/" + file_name)

		for i in range(len(df)):
			bigram += nltk.bigrams(df['BODY'][i].split())

		fdist = nltk.FreqDist(bigram)

		for gram, freq in fdist.most_common(100):
			output.append(gram)
		create_file = "../bigram_data/bigram_"+file_name 
		resultFile = open(create_file,'wb')
		wr = csv.writer(resultFile,dialect='excel')
		wr.writerows(output)

if __name__ == "__main__":
	f = get_files()
	bigram_generator(f)

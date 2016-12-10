import re
import operator
from collections import Counter

from numpy import array
from scipy import zeros

from sklearn import svm
import csv

kWORDS = re.compile("[a-z]{1,}")

kSTOPWORDS = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'yo','your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his','himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself','they', 'them', 'their', 'theirs', 'themselves', 'what', 'which','who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are','was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having','do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if','or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for','with', 'about', 'against', 'between', 'into', 'through', 'during','before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in','out', 'on', 'off', 'over', 'under', 'again', 'further', 'then','once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any','both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no','nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very','s', 't', 'can', 'will', 'just', 'don', 'should', 'now', 've', 'm'])


def tokenize(sentence):
	return kWORDS.findall(sentence)

def bigrams(sentence):
	for ii, ww in enumerate(sentence[:-1]):
		yield ww, sentence[ii +1]




class Bigrams:
	def __init__(self, exclude=[]):
		self._vocab = Counter()
		self._exclude = set(exclude)
		self._bigrams = {}

	def vocab_build(self,sentence):
		for ii in sentence:
			self._vocab[ii] += 1

	
if __name__=="__main__":
	upvotes = []
	upvoteBody = []
	myfile = csv.reader(open('../Data/raw_data/formatted_data/100k_upvotes_formatted.csv'), delimiter=",")
	for row in myfile:
		upvotes.append(int(row[0]))
		upvoteBody.append(row[1])
	
	trainingData = Bigrams(exclude=kSTOPWORDS)
	for row in upvoteBody:
		trainingData.vocab_build(tokenize(row))
	print(trainingData._vocab)

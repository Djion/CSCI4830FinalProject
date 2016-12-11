'''
Joshua Zepf, Alex Ring, Richard Dyer, Cameron Tierney
November/December 2016

Program uses a bigram model and data from Reddit comments to predict whether a
comment will be upvoted or downvoted. This program is the same as svm.py, except
it has a smaller data set to make for speedy testing. This file should not be
used to actually predict, it is just to make sure code is working correctly.
'''

from sklearn import svm
import numpy
from numpy import genfromtxt

upvotes_body = genfromtxt("../Data/raw_data/formatted_data/100k_upvotes_formatted.csv", delimiter=",", dtype=None, skip_header=1, usecols=(1), max_rows=10000)
upvotes_score = genfromtxt("../Data/raw_data/formatted_data/100k_upvotes_formatted.csv", delimiter=",", dtype=None, skip_header=1, usecols=(0), max_rows=10000)

downvotes_body = genfromtxt("../Data/raw_data/formatted_data/100k_downvotes_formatted.csv", delimiter=',', dtype=None, skip_header=1, usecols=(1), max_rows=10000)
downvotes_score = genfromtxt("../Data/raw_data/formatted_data/100k_downvotes_formatted.csv", delimiter=',', dtype=None, skip_header=1, usecols=(0), max_rows=10000)

# CHANGE THE PATH OF THE FOLLOWING LINE TO CHANGE BETWEEN N-GRAMS
#bigrams = genfromtxt("../Feature_Extraction/unigram_data/unigram_100k_upvotes_formatted.csv", dtype=None)
bigrams = genfromtxt("../Feature_Extraction/bigram_data/bg_combo.csv", dtype=None)
#bigrams = genfromtxt("../Feature_Extraction/trigram_data/trigram_combo.csv", dtype=None)
for i in range(len(bigrams)):
    bigrams[i] = bigrams[i].replace(",", " ")
    bigrams[i] = bigrams[i].lower()

train_set_len = 7000 # 70% of 10000 submissions
train_set_features = numpy.zeros(shape=(train_set_len, len(bigrams)))
train_set_score = numpy.zeros(shape=train_set_len)

for a in range(3500):
    comment = upvotes_body[a]
    for i in range(len(bigrams)):
        bigram = bigrams[i]
        num_found = comment.count(bigram)
        train_set_features[a][i] = num_found
        '''
        if (num_found != 0):
            print("hit")
        '''
    train_set_score[a] = 1
for b in range(3500):
    comment = downvotes_body[b]
    for i in range(len(bigrams)):
        bigram = bigrams[i]
        num_found = comment.count(bigram)
        train_set_features[a + b + 1][i] = num_found
        '''
        if (num_found != 0):
            print("hit")
        '''
    train_set_score[a + b + 1] = -1

print("\nTraining Set Feature Arrays:")
print(train_set_features)
print("\nTraining Set Score Array")
print(train_set_score)

classifier = svm.SVC()
print("\nClassifier:")
print(classifier.fit(train_set_features, train_set_score))

test_set_len = 3000 # 30% of 10000 submissions
test_set_features = numpy.zeros(shape=(test_set_len, len(bigrams)))
test_set_score = numpy.zeros(shape=test_set_len)

for c in range(1500):
    comment = upvotes_body[a + c + 1]
    for i in range(len(bigrams)):
        bigram = bigrams[i]
        num_found = comment.count(bigram)
        test_set_features[c][i] = num_found
        '''
        if (num_found != 0):
            print("hit")
        '''
    test_set_score[c] = 1
for d in range(1500):
    comment = downvotes_body[b + d + 1]
    for i in range(len(bigrams)):
        bigram = bigrams[i]
        num_found = comment.count(bigram)
        test_set_features[c + d + 1][i] = num_found
        '''
        if (num_found != 0):
            print("hit")
        '''
    test_set_score[c + d + 1] = -1

print("\nTest Set Feature Arrays:")
print(test_set_features)
print("\nTest Set Score Arrays:")
print(test_set_score)

num_right = 0.0
num_down_predicted = 0.0
num_up_predicted = 0.0
num_up_c = 0.0
num_down_c = 0.0
for n in range(test_set_len):
    z = classifier.predict(test_set_features[n].reshape(1, -1))
    if z == -1:
        num_down_predicted += 1
    else:
        num_up_predicted += 1
    if z == test_set_score[n]:
        num_right += 1
        if z == -1:
            num_down_c += 1
        else:
            num_up_c += 1

up_percent = (num_up_predicted / test_set_len) * 100
down_percent = (num_down_predicted / test_set_len) * 100
accuracy = (num_right / test_set_len) * 100
print("Number Right:")
print(num_right)
print("Number of upvotes predicted:")
print(num_up_predicted)
print("Percentage of upvotes predicted:")
print(up_percent)
print("Number of downvotes predicted:")
print(num_down_predicted)
print("Percentage of downvotes predicted:")
print(down_percent)
print("Accuracy:")
print(accuracy)

print("Number of downvotes correctly predicted: ")
print(num_down_c)
print("Number of upvotes correctly predicted: ")
print(num_up_c)

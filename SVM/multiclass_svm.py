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

num_negone = 0
num_zero = 0
num_one = 0
num_two = 0
for i in range(len(upvotes_score)):
    if upvotes_score[i] >= 1 and upvotes_score[i] < 2500:
        upvotes_score[i] = 1
        num_one += 1
    elif upvotes_score[i] >= 2500:
        upvotes_score[i] = 4
        num_two += 1
for i in range(len(downvotes_score)):
    if downvotes_score[i] == 0:
        downvotes_score[i] = 0
        num_zero += 1
    elif downvotes_score[i] <= -1:
        downvotes_score[i] = -1
        num_negone += 1

# CHANGE THE PATH OF THE FOLLOWING LINE TO CHANGE BETWEEN N-GRAMS
#bigrams = genfromtxt("../Feature_Extraction/unigram_data/unigram_100k_upvotes_formatted.csv", dtype=None)
bigrams = genfromtxt("../Feature_Extraction/bigram_data/bg_combo.csv", dtype=None)
trigrams = genfromtxt("../Feature_Extraction/trigram_data/trigram_combo.csv", dtype=None)
for i in range(len(bigrams)):
    bigrams[i] = bigrams[i].replace(",", " ")
    bigrams[i] = bigrams[i].lower()
for i in range(len(trigrams)):
    trigrams[i] = trigrams[i].replace(",", " ")
    trigrams[i] = trigrams[i].lower()

train_set_len = 7000 # 70% of 10000 submissions
train_set_features = numpy.zeros(shape=(train_set_len, len(bigrams) + len(trigrams)))
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
    for j in range(len(trigrams)):
        trigram = trigrams[j]
        num_found = comment.count(trigram)
        train_set_features[a][j] = num_found
    train_set_score[a] = upvotes_score[a]
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
    for j in range(len(trigrams)):
        trigram = trigrams[j]
        num_found = comment.count(trigram)
        train_set_features[a + b + 1][j] = num_found
    train_set_score[a + b + 1] = downvotes_score[a]

print("\nTraining Set Feature Arrays:")
print(train_set_features)
print("\nTraining Set Score Array")
print(train_set_score)

classifier = svm.SVC()
print("\nClassifier:")
print(classifier.fit(train_set_features, train_set_score))

test_set_len = 3000 # 30% of 10000 submissions
test_set_features = numpy.zeros(shape=(test_set_len, len(bigrams) + len(trigrams)))
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
    for j in range(len(trigrams)):
        trigram = trigrams[j]
        num_found = comment.count(trigram)
        train_set_features[c][j] = num_found
    test_set_score[c] = upvotes_score[a + c + 1]
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
    for j in range(len(trigrams)):
        trigram = trigrams[j]
        num_found = comment.count(trigram)
        train_set_features[c + d + 1][j] = num_found
    test_set_score[c + d + 1] = downvotes_score[b + d + 1]

print("\nTest Set Feature Arrays:")
print(test_set_features)
print("\nTest Set Score Arrays:")
print(test_set_score)

num_right = 0.0
pnum_negone = 0.0
pnum_zero = 0.0
pnum_one = 0.0
pnum_two = 0.0
pnum_negone_c = 0.0
pnum_zero_c = 0.0
pnum_one_c = 0.0
pnum_two_c = 0.0
for n in range(test_set_len):
    z = classifier.predict(test_set_features[n].reshape(1, -1))
    if z == test_set_score[n]:
        num_right += 1
        if z == -1:
            pnum_negone_c += 1
        elif z == 0:
            pnum_zero_c += 1
        elif z == 1:
            pnum_one_c += 1
        elif z == 2:
            pnum_two_c += 1
    if z == -1:
        pnum_negone += 1
    elif z == 0:
        pnum_zero += 1
    elif z == 1:
        pnum_one += 2
    elif z == 2:
        pnum_two += 1
accuracy = (num_right / test_set_len) * 100
print("Number Right:")
print(num_right)
print("Accuracy:")
print(accuracy)


print("Number of Class -1 Predicted: ", pnum_negone)
print("Number of Class -1 Predicted Correctly: ", pnum_negone_c)
print("Accuracy at Predicting Class -1: ", ((pnum_negone_c / num_negone) * 100))

print("Number of Class 0 Predicted: ", pnum_zero)
print("Number of Class 0 Predicted Correctly: ", pnum_zero_c)
print("Accuracy at Predicting Class 0: ", ((pnum_zero_c / num_zero) * 100))

print("Number of Class 1 Predicted: ", pnum_one)
print("Number of Class 1 Predicted Correctly: ", pnum_one_c)
print("Accuracy at Predicing Class 1: ", ((pnum_one_c / num_one) * 100))

print("Number of Class 2 Predicted: ", pnum_two)
print("Number of Class 2 Predicted Correctly: ", pnum_two_c)
print("Accuracy at Predicting Class 2: ", ((pnum_two_c / num_two) * 100))

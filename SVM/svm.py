'''
Joshua Zepf, Alex Ring, Richard Dyer, Cameron Tierney
November/December 2016

Program uses a bigram model and data from Reddit comments to predict whether a
comment will be upvoted or downvoted
'''

from sklearn import svm
import numpy
from numpy import genfromtxt

# Extract upvote comments and scores
upvotes_body = genfromtxt("../Data/raw_data/formatted_data/100k_upvotes_formatted.csv", delimiter=',', dtype=None, skip_header=1, usecols=(1))
upvotes_score = genfromtxt("../Data/raw_data/formatted_data/100k_upvotes_formatted.csv", delimiter=',', dtype=None, skip_header=1, usecols=(0))

# Extract downvote comments and scores
downvotes_body = genfromtxt("../Data/raw_data/formatted_data/100k_downvotes_formatted.csv", delimiter=',', dtype=None, skip_header=1, usecols=(1))
downvotes_score = genfromtxt("../Data/raw_data/formatted_data/100k_downvotes_formatted.csv", delimiter=',', dtype=None, skip_header=1, usecols=(0))

# Extract bigram data
bigrams = genfromtxt("../Feature_Extraction/bigram_data/bigram_100k_Pics_100upvotes.csv", dtype=None)
for i in range(len(bigrams)):
    bigrams[i] = bigrams[i].replace(",", " ")
    bigrams[i] = bigrams[i].lower()

# Size of Upvote Data: 10005
# Size of Downvote Data: 100046
# Set up training set arrays and size
train_set_len = (7003 + 70032) # 70% of Upvote Data + 70% of Downvote Data
train_set_features = numpy.zeros(shape=(train_set_len, len(bigrams)))
train_set_score = numpy.zeros(shape=train_set_len)

# Count bigrams and create feature arrays for upvotes training set
for a in range(7003):
    comment = upvotes_body[a]
    for i in range(len(bigrams)):
        bigram = bigrams[i]
        num_found = comment.count(bigram)
        train_set_features[a][i] = num_found
    train_set_score[a] = 1
# Count bigrams and create feature arrays for downvotes training set
for b in range(70032):
    comment = downvotes_body[b]
    for i in range(len(bigrams)):
        bigram = bigrams[i]
        num_found = comment.count(bigram)
        train_set_features[a + b + 1][i] = num_found
    train_set_score[a + b + 1] = -1

classifier = svm.SVC()
print("\nClassifier:")
print(classifier.fit(train_set_features, train_set_score))

# Set up test set
test_set_len = 3002 + 30014 # 30% of Upvote Data + 30% of Downvote Data
test_set_features = numpy.zeros(shape=(test_set_len, len(bigrams)))
test_set_score = numpy.zeros(shape=test_set_len)

# Count bigrams and create feature arrays for upvotes test set
for c in range(3002):
    comment = upvotes_body[a + c + 1]
    for i in range(len(bigrams)):
        bigram = bigrams[i]
        num_found = comment.count(bigram)
        test_set_features[c][i] = num_found
    test_set_score[c] = 1
# Count bigrams and create feature arrays for upvotes test set
for d in range(30014):
    comment = downvotes_body[b + d + 1]
    for i in range(len(bigrams)):
        bigram = bigrams[i]
        num_found = comment.count(bigram)
        test_set_features[c + d + 1][i] = num_found
    test_set_score[c + d + 1] = -1

# Use test set to make predictions and count the number correctly predicted
num_right = 0
num_down_predicted = 0
num_up_predicted = 0
for n in range(test_set_len):
    z = classifier.predict(test_set_features[n].reshape(1, -1))
    if z == -1:
        num_down_predicted += 1
    else:
        num_up_predicted += 1
    if z == test_set_score[n]:
        num_right += 1

up_percent = num_up_predicted / test_set_len
down_percent = num_down_predicted / test_set_len
accuracy = num_right / test_set_len
print("\nNumber of Upvotes Predicted: ", up_percent, "%")
print("Number of Downvotes Predicted: ", down_percent, "%")
print("Accuracy: ", accuracy, "%")

#Author: Richard Dyer
import random
import sys
sys.path.insert(0, "../Data/scripts")
from csv import DictReader
from format import *

#########################################################################################
#Generates testing and training data, formatted according to vowpal wabbit specifications
#########################################################################################

def formatLine(line, label):
    line = remove_urls(line)
    line = stringFormat(line)
    return label + ' | ' + line.replace(' ',' | ')

if __name__ == "__main__":
    posdata = open("../Data/raw_data/100k_Askreddit_100upvotes.csv", encoding='utf-8', errors='ignore')
    negdata = open("../Data/raw_data/100k_Askreddit_10downvotes.csv", encoding='utf-8', errors='ignore')
    train = open("train.vw", 'w')
    test = open("test.vw", 'w')
    pos = DictReader(posdata)
    i = 0
    for row in pos:
        if (random.randint(0, 9) == 0):
            test.write(formatLine(row['BODY'], '1') + '\n')
        else:
            train.write(formatLine(row['BODY'], '1') + '\n')
    neg = DictReader(negdata)
    for row in neg:
        if (random.randint(0, 9) == 0):
            try:
                test.write(formatLine(row['BODY'], '-1') + '\n')
            except TypeError:
                i += 1
        else:
            try:
                train.write(formatLine(row['BODY'], '-1') + '\n')
            except TypeError:
                i += 1
    print(i, "lines omitted for errors.")
    posdata.close()
    negdata.close()
    train.close()
    test.close()

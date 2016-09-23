
from sklearn import svm
import csv
from Essay import Essay
import codecs
#from Features import Features

if __name__ == '__main__':
    feature_vector = []
    scores = []
    vector = []

    # To Do: Change file name
    training_data = 'dataset/training_set_rel3.tsv'
    with codecs.open(training_data,encoding='utf-8',errors='ignore') as tsvfile:
        tsvfile = csv.reader(tsvfile, delimiter = '\t')
        line = 0
        for row in tsvfile:
            # Ignore the heading line
            if line == 0:
                line += 1
                continue

            e = Essay(row, store_score = True)
            f = e.features
            for i in sorted(f.__dict__.keys()):
                vector.append(f.__dict__[i])
            scores.append(e.score)
            feature_vector.append(vector)

    clf = svm.SVR()
    clf.fit(feature_vector, scores)
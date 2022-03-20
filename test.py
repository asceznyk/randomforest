from random import seed
from math import sqrt

from utils import *
from rfc import * 

dataset = load_csv('sonar.csv')
for i in range(0, len(dataset[0])-1):
    str_column_to_float(dataset, i)
str_column_to_int(dataset, len(dataset[0])-1)

train, test = train_test_split(dataset)

print(len(dataset))
print(len(train), len(test))

n_features = int(sqrt(len(dataset[0])-1))
n_est = 10
max_depth = 10
n_folds = 5

scores = evaluate_algorithm(dataset, random_forest, bag, n_folds, n_est, max_depth, n_features)

print(f"hyperparameters n_est={n_est}, n_features={n_features}, max_depth={max_depth}")

avg_acc = sum(scores)/len(scores)

print(scores)
print(f"mean accuracy on 5 folds: {(avg_acc * 100.0):.3f}%")

#train_acc = accuracy_score([row[-1] for row in train], [bag(rfc, row) for row in train])
#test_acc = accuracy_score([row[-1] for row in test], [bag(rfc, row) for row in test])
#print(train_acc, test_acc)


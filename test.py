from random import seed

from utils import *
from rfc import * 

seed(2)

dataset = load_csv('sonar.csv')
for i in range(0, len(dataset[0])-1):
    str_column_to_float(dataset, i)
str_column_to_int(dataset, len(dataset[0])-1)

n_features = len(dataset[0])-1
tree = build_tree(dataset, n_features, 1, 10)
print(bag([tree], dataset[0]), bag([tree], dataset[1]))

#train, test = train_test_split(dataset)
#print(len(train), len(test))


import math
import numpy as np

from random import randrange
from csv import reader

def load_csv(filename):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    
    return dataset

def str_column_to_float(dataset, column):
    for row in dataset: row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    
    return lookup

def train_test_split(dataset, split=0.2): 
    idxs_train = []
    while len(idxs_train) < math.floor((1 - split) * len(dataset)):
        i = randrange(len(dataset))
        if i not in idxs_train:
            idxs_train.append(i)

    dataset = np.array(dataset)
    idxs_test = [i for i in range(len(dataset)) if i not in idxs_train]
    train = dataset[idxs_train]
    test = dataset[idxs_test]
    dataset = dataset.tolist()

    return train, test

def accuracy_score(labels, predicted):
    count = 0
    for y, p in zip(labels, predicted):
        if y == p: count += 1
    return count/len(labels)

def cross_validation_split(dataset, n_folds):
    dataset_split = []
    dataset_copy = list(dataset)

    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = []
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    
    return dataset_split

def evaluate_algorithm(dataset, algorithm, f_pred, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None

        model = algorithm(train_set, *args)
        accuracy = accuracy_score([row[-1] for row in fold], [f_pred(model, row) for row in fold])
        scores.append(accuracy)
    return scores

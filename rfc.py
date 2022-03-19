from random import seed, randrange
from csv import reader
from math import sqrt

def class_values(dataset):
    return list(set(row[-1] for row in dataset))

def attr_split(attr, value, dataset):
    left, right = [], []
    for row in dataset:
        if row[attr] < value:
            left.append(row)
        else:
            right.append(row)
    
    return left, right

def gini_index(groups, classes):
    n_instances = float(sum([len(group) for group in groups]))
    
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0.0: continue
        score = 0.0
        for c in classes:
             p = [row[-1] for row in group].count(c) / size
             score += p*p
        gini += (1.0 - score) * (size / n_instances)
    
    return gini

def count_classify(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

def best_split(dataset, n_features):
    classes = class_values(dataset)
    b_attr, b_value, b_score, b_groups = 999, 999, 999, None

    features = []
    while len(features) < n_features:
        f = randrange(len(dataset[0])-1) 
        if f not in features: 
            features.append(f) 
    
    for attr in features:
        for row in dataset:
            groups = attr_split(attr, row[attr], dataset)
            gini = gini_index(groups, classes)
            if gini < b_score:
                b_attr, b_value, b_score, b_groups = attr, row[attr], gini, groups
    
    return {'attr': b_attr, 'value': b_value, 'groups':b_groups}

def binary_split(node, n_features, min_size, max_depth, depth):
    left, right = node['groups']
    del node['groups']

    if not left or not right: 
        node['left'] = node['right'] = count_classify(left+right)
        return

    if depth >= max_depth:
        node['left'], node['right'] = count_classify(left), count_classify(right)
        return

    if len(left) <= min_size:
        node['left'] = count_classify(left)
    else:
        node['left'] = best_split(left, n_features)
        binary_split(node['left'], n_features, min_size, max_depth, depth+1)

    if len(right) <= min_size:
        node['right'] = count_classify(right)
    else:
        node['right'] = best_split(right, n_features)
        binary_split(node['right'], n_features, min_size, max_depth, depth+1)

def build_tree(dataset, n_features,  min_size, max_depth):
    root = best_split(dataset, n_features)
    binary_split(root, n_features, min_size, max_depth, 1)
    return root








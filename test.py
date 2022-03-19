from random import seed
from rfc import * 

seed(2)
dataset = load_csv('sonar.csv')
for i in range(0, len(dataset[0])-1):
    str_column_to_float(dataset, i)
str_column_to_int(dataset, len(dataset[0])-1)



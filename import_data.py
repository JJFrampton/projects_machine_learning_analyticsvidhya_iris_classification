#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

headings = ['sepal_length_cm',
'sepal_width_cm',
'petal_length_cm',
'petal_width_cm',
'class']

raw_data = pd.read_csv('./iris.data')

df = pd.DataFrame(raw_data)
# df = pd.DataFrame(raw_data, columns=headings)
df.columns = headings
print(df.columns)

# print(df.head(3))
# print(df.mean(0))
# print(df.min(0))
# print(df.count())
# print(df.shape)
# print(df.describe())

# print(df.info())

# print('sepal_length_cm')
# print('mean : ', df['sepal_length_cm'].describe()[1])
# print('std : ', df['sepal_length_cm'].describe()[2])
# print('sepal_width_cm')
# print('mean : ', df['sepal_width_cm'].describe()[1])
# print('std : ', df['sepal_width_cm'].describe()[2])
# print('petal_length_cm')
# print('mean : ', df['petal_length_cm'].describe()[1])
# print('std : ', df['petal_length_cm'].describe()[2])
# print('petal_width_cm')
# print('mean : ', df['petal_width_cm'].describe()[1])
# print('std : ', df['petal_width_cm'].describe()[2])

classes = df['class'].unique()
print(df['class'].unique())

print(classes[0])
# class1 = df['class' = classes[0]]
# print('mean : ', class1.describe()[1])

# print('std : ', classes[0].describe()[2])
# print(classes[1])
# print('mean : ', classes[1].describe()[1])
# print('std : ', classes[1].describe()[2])
# print(classes[2])
# print('mean : ', classes[2].describe()[1])
# print('std : ', classes[2].describe()[2])

class1 = df[df['class'] == classes[0]]
class2 = df[df['class'] == classes[1]]
class3 = df[df['class'] == classes[2]]

print(classes[0])
print('mean : \n', class1.mean())
# print('std  : ', class1.std())
print(classes[1])
print('mean : \n', class2.mean())
# print('std  : ', class2.describe())
print(classes[2])
print('mean : \n', class3.mean())
# print('std  : ', class3.describe())

classDf = df.groupby(by=['class'])
print(classDf.mean())
plt.plot(classDf.mean())
plt.show()
plt.savefig('plot_test.png')

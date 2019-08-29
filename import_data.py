#!/usr/bin/env python3

import pandas as pd

headings = ['sepal_length_cm',
'sepal_width_cm',
'petal_length_cm',
'petal_width_cm',
'class']

raw_data = pd.read_csv('./iris.data')

df = pd.DataFrame(raw_data)
# df = pd.DataFrame(raw_data, columns=headings)
df.columns = headings

print(df.head(3))
print(df.mean(0))
print(df.min(0))
print(df.count())
print(df.shape)
print(df.describe())

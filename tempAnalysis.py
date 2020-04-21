# Using information from 
# https://realpython.com/python-csv/
# https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
# https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673


# import the pandas library
import pandas as pd
# import the numpy library
import numpy as np

# using pandas.read_csv will return a dataframe object for the data in the iris.data file
df = pd.read_csv("iris.data")
# print(df)

df.columns
# provides an array of the headings for the data

for col_name in df.columns:
    print(col_name)


print(df.median())
print(df.mean())
print(df.std())
print(df.max())
print(df.min())
print(df.corr())


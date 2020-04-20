# Using information from 
# https://realpython.com/python-csv/
# https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/


# import the pandas library
import pandas
# using read_csv will return a dataframe object for the data in the iris.data file
df = pandas.read_csv("iris.data")
#print(df)

mean1 = df["sepal length"].mean()
print(mean1)
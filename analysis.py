# this script will complete a number of tasks including:
# output a summary of each variable from the iris data to a single text file
# output a histogram of each variable - these will be saved a png files 
# output a scatter plot of each pair of variables

# Using information from 
# https://realpython.com/python-csv/
# https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
# https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673


# import the pandas library
import pandas as pd
# import the numpy library
import numpy as np
# in order to direct the output to a text file I also import sys 
import sys

# using pandas.read_csv will return a dataframe object for the data in the iris.data file
df = pd.read_csv("iris.data")
# print(df)

print("")
print("The following is an overview of the Iris Data Set available at http://archive.ics.uci.edu/ml/datasets/Iris")
print("")
# The addition of the printed "" helps to improve readabilty of the output and is used throughout the script

df.columns
# provides an array of the headings for the data

for col_name in df.columns[0:4]:
    # this will isolate the four variables that include length and width
    # the for loop will iterate though the following statistics for each column as defined by the dataframe above
    print("The variable", col_name, "has the following results:")
    print("The median is", df[col_name].median(),"cm")
    print("The mean is", round(df[col_name].mean(),4),"cm") 
    print("The standard deviation is", round(df[col_name].std(),4))
    # both mean and standard deviation are rounded to 4 decimal places
    print("The maximum value is", df[col_name].max(),"cm")
    print("The minimum value is", df[col_name].min(),"cm") 
    print("")

print("The following classes of iris flowers are represented in this data: ")
print("")
print(df.groupby(["class"]).count())
# in order to see the division of the types of flowers within the data
print ("")
print("The following matrix examines the relationships between the variables (where +/-1 is a strong relationship and 0 indicates no relationship):")
print("")
print(df.corr())
# This provides a correlation matrix between the variables

#sys.stdout = open("summary_results.txt", "wt")


#outF = open("summary_results.txt", "w")
#outF.writelines()
#outF.close()
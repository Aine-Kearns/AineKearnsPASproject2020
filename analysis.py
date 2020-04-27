# This script will complete a number of tasks including:
# output a summary of each variable from the iris data to a single text file
# output a histogram of each variable - these will be saved a png files 
# output a scatter plot of each pair of variables

# Using information from 
# https://realpython.com/python-csv/
# https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
# https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot
# https://www.python-course.eu/sys_module.php


import pandas as pd
# in order to open the data file and complete calcuations  
import sys
# this will allow me to export to output the summary of each variable to a single text file
import matplotlib.pyplot as plt
# will allow for the creation of histograms


df = pd.read_csv("iris.data")
# using pandas.read_csv will return a dataframe object for the data in the iris.data file


print(df.describe())
# this will provide a set of summary statistics for each of the variables
save_stdout = sys.stdout
outF = open("summary_of_variables.txt", "w")
sys.stdout = outF
print("The following is an overview of the Iris Data Set available at http://archive.ics.uci.edu/ml/datasets/Iris")
print("")
print(df.describe())
sys.stdout = save_stdout
outF.close()
# this code will allow me to capture the output of the df.describe() function and write it to a file in the current folder


df.columns
# provides an array of the headings for the data

for col_name in df.columns[0:4]:
    # this will isolate the four variables that include length and width
    # the for loop will iterate through and develop histograms for each column as defined by the dataframe above
    plt.hist(df[col_name])
    # create a histogram for each of the four variables
    plt.title(col_name)
    plt.xlabel("measured in centimetres")
    plt.ylabel("Iris numbers")
    plt.savefig(col_name)
    plt.clf()
    

import seaborn as sns
# this library of plots that I can use to provide pair plots
sns.set(style="ticks", color_codes=True)
sns.pairplot(df, hue="class")
plt.savefig("iris_data_pairplots.png")
plt.show()
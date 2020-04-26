# this script will complete a number of tasks including:
# output a summary of each variable from the iris data to a single text file
# output a histogram of each variable - these will be saved a png files 
# output a scatter plot of each pair of variables

# Using information from 
# https://realpython.com/python-csv/
# https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
# https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot
# https://www.python-course.eu/sys_module.php

# import the pandas library
import pandas as pd
# import the numpy library
import numpy as np
# in order to direct the output to a text file I also import sys 
import sys
import matplotlib.pyplot as plt



# using pandas.read_csv will return a dataframe object for the data in the iris.data file
df = pd.read_csv("iris.data")


print(df.describe())
save_stdout = sys.stdout
outF = open("summary_of_variables.txt", "w")
sys.stdout = outF
print("The following is an overview of the Iris Data Set available at http://archive.ics.uci.edu/ml/datasets/Iris")
print("")
print(df.describe())
sys.stdout = save_stdout
outF.close()


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
    #plt.show()
    plt.clf()
    



#import seaborn as sns
#sns.set(style="ticks", color_codes=True)
#iris = sns.load_dataset("iris.data")
#g = sns.pairplot(iris, hue="class")

#plt.plot(df["sepal length"]),(df["sepal width"], "b")
#plt.plot(df["petal length"]),(df["petal width"], "r")
#plt.plot(df["sepal length"]),(df["petal length"], "b")
#plt.plot(df["sepal width"]),(df["petal width"], "b")

#plt.show()
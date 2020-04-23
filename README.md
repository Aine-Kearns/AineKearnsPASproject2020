# AineKearnsPASproject2020
Project Plan for Programming and Scripting GMIT 2020
- In order to complete this project I will need to complete the following tasks:
  - Import a data file into the analysis.py script and add the pandas and numpy libraries which will allow me to complete statistical calculations and create graphs
  - Define the calculations that will be presented for summary statistics and establish how to calculate this using a for loop
  - The statistical calculations above are only relevant for the ordinal data, simple count measures will be used for the nominal data (i.e. the class)
  - Write additional code into the script to output the summary statistics to a single text file 
  - Using numpy I will create histograms for each variable and save these as png files
  - I will also create scatter plots for each pair of variables 

# Updates made
## 23rd April 2020
* As noted in the project plan, statistical measures are not relevant for the class of flowers so a matrix of summary data was created using groupby and count from the pandas library
* Further work today on the script and attempted to create histograms for each variable using matplotlib.pyplot but while reviewing lectures I realise I have overcomplicated the task but using the "for loop" for the summary of the variables rather than df.describe() - which I had overlooked.  I need to step back and see if I should go down the route I've started or begin fresh.
## 22nd April 2020
* Added a "for loop" into the script, this "for loop" will iterate through the columns to calculate the statistics for each variable
* Copied this code from the tempAnalysis.py file (which will be removed from repository) into the analysis.py file
* Added in a statistic to examine the correlations between the variables 
## 21st April 2020
* Established how to calculate summary statistics for data using information from [https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673]
* Added this into the script
* Also imported the numpy library into the script as this will be used for later objectives
* Attempted to introduce for loops into the script to begin to summarise the stats for each variable in groups of variables
## 20th April 2020
* Updated iris.data file to add headings as per additional documentation on [http://archive.ics.uci.edu/ml/datasets/Iris]
* Established how to read and print CSV files by importing CSV library and pandas, using the following websites
  * [https://realpython.com/python-csv/]
  * [https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/]
* Created a second file called tempAnalysis.py to test out how to calculate stats 
## 19th April 2020
* Created Repository and found Iris Data file on http://archive.ics.uci.edu/ml/datasets/Iris
* Added data set to repository
* Created a python script file called analysis.py and began to define the problems to be address
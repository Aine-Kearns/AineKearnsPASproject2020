# AineKearnsPASproject2020
**Project Plan for Programming and Scripting GMIT 2020**
- In order to complete this project I will need to complete the following tasks:
  - Import a data file into the **analysis.py** script and add the pandas and matplotlib libraries which will allow me to complete statistical calculations and create graphs
  - Define the calculations that will be presented with summary statistics and establish how to calculate these
  - Write additional code into the script to output the summary statistics to a single text file 
  - Using a "For Loop" I will create histograms for each variable and save these as .png files
  - I will also create scatter plots for each pair of variables using the seaborn module <br>

**Overview of python script**
- The python script developed for this project is called **analysis.py** and it is made up of 5 sections which are outlined below reflecting their order in the script
  1. Import initial modules to be used in the script including pandas, sys and matplotlib 
  2. Use pandas module to open and read the data file iris.data (which is saved in the repository) as a csv file in order to complete sections 3 - 5 of the script
  3. Print the summary statistics using df.describe() and save this output to a text file called *summary_of_variables.txt* using the sys module
  4. Create and save histograms for each of the variables using a "For Loop" and the matplotlib module - each file is named after the associated variable i.e. *sepal length.png, sepal width.png, petal length.png, petal width.png* 
  5. Import seaborn and using this module create, save and print the scatterplots for pair of variables - file saved as *iris_data_pairplots.png*<br>

**Iris Data Set**
- The Iris Dataset is a well known dataset that was created by Ronald Fisher in 1936.  Fisher was a statistician and biologist and he used this dataset in his paper *The use of multiple measurements in taxonomic problems*.  The data was actually gathered by Edgar Anderson who was attempting to quantify variation associated with three related species of iris flowers. The dataset consists of 50 samples of each of the three species (*Iris setosa, Iris virginica and Iris veriscolor*) and four features were measured, all in centimeters: the length and the width of both the sepal and the petal.  Fisher used this data to develop a linear discriminant model to distinguish the species from each other  [https://en.wikipedia.org/wiki/Iris_flower_data_set].
# Updates made
## 27th April 2020
* Removed the import numpy command as this is not required in the current script
* Established how to save the seaborn pairplots as a .png file in the folder but in order to do this I needed to change the order of the script so the plt.show() command was last
* Removed tempAnalysis.py from the repository - this was being used only to test changes 
* Removed the matrix that was added on April 23rd - this is not required for the analysis
## 26th April 2020
* Using information from [https://www.python-course.eu/sys_module.php] I've managed to save the output from df.describe() to a .txt file within the folder
* I've decided to now remove the summary of variables under the "for loop" as noted on the notes from April 23rd, in this way the code is now reduced and easier to read 
* I've updated some information above adding in the section on the Iris Data Set   
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
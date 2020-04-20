# this script will complete a number of tasks including
# output a summary of each variable from the iris data to a single text file
# output a histogram of each variable - these will be saved a png files 
# output a scatter plot of each pair of variables

import csv
# import the csv library 

with open("iris.data") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)} ')
            line_count += 1
        else:
            print(f'Sepal length is {row[0]}, sepal width is {row[1]}, petal length is {row[2]}, petal width is {row[3]} and the iris class is {row[4]} ')
            line_count += 1
        print(f"Processed {line_count} lines.")
print("This is the end.")
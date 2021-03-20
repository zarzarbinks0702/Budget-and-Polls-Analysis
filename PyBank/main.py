import os
import csv

#link to the csv data file for pybank project
csvpath = os.path.join("Resources", "budget_data.csv")

#set the initial row count to 0 to determine the total number of months
row_count = 0

#open csv data file for pybank project and make it readable
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #adds one to the row count for each row
    for row in csvreader:
        row_count += 1

#print total months as rows minus 1 since one of the rows is the header row
print(f"Total Months: {row_count - 1}")

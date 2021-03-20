import os
import csv

#link to the csv data file for pybank project
csvpath = os.path.join("Resources", "budget_data.csv")

#set the initial row count to 0 to determine the total number of months
row_count = 0
#set the initial value fro total profits
total_profits = 0
#array for the values of the profits/losses column
profits_and_losses = []

#open csv data file for pybank project and make it readable
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #pulls header row out
    csv_header = next(csvreader)
    #for each row in the csv file
    for row in csvreader:
        #adds one to the row count for each row
        row_count += 1
        #adds the profits/losses to previous total
        total_profits += int(row[1])
        #appends each value in the profits/losses column to the profits_and_losses array
        profits_and_losses.append(int(row[1]))

#print total months as rows
print(f"Total Months: {row_count}")
print(f"Net Profits: ${total_profits}")

import os
import csv

#link to the csv data file for pybank project
pybank_csv = os.path.join("Resources", "budget_data.csv")

#set the initial row count to 0 to determine the total number of months
row_count = 0
#set the initial value for total profits
total_profits = 0
#array for the values of the profits/losses column
profits_and_losses = []
#array for the changes in profits and Losses
change_in_profits = []

#open csv data file for pybank project and make it readable
with open (pybank_csv, newline='') as csvfile:
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
        profits_and_losses.append(row[1])

#creating amended lists of profits_and losses - one without the first value and one without the last value to zip and calculate the change in profits
profits_and_losses_no_first = profits_and_losses[1:]
profits_and_losses_no_last = profits_and_losses[:-1]

#zip the new profits_and_losses lists together to form one list - and converting it to proper form
new_profits_and_losses = list(zip(profits_and_losses_no_last, profits_and_losses_no_first))

#goes through the new_profits_and losses list
for set in new_profits_and_losses:
    #calculates the change between the values stored in each list item
    change = int(set[1]) - int(set[0])
    #adds the new value to the change in profits list
    change_in_profits.append(int(change))

#takes the change_in profits list
for change in change_in_profits:
    #set a starting variable to hold the sum of all the changes
    sum_of_changes = 0
    #add each value together
    sum_of_changes += int(change)
    #divide the sum by the length on the change_in_profits list to find the average change
    avg_change = sum_of_changes / len(change_in_profits)

#print total months as rows
print(f"Total Months: {row_count}")
#prints the net profits
print(f"Net Profits: ${total_profits}")
#prints the average change in profits/Losses, rounded to 2 decimal places (since we're dealing with money)
print(f"Average Change: ${round(avg_change, 2)}")

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

#sorting the change_in_profits list
sorted_change_in_profits = sorted(change_in_profits)

#defining the greatest increase and decrease in profits using the sorted_change_in_profits list
greatest_increase = sorted_change_in_profits[-1]
greatest_decrease = sorted_change_in_profits[0]

#searching the original change_in_profits for the index of the changes
for change in change_in_profits:
    if change == greatest_increase:
        #saves the index to a new variable
        index_greatest_increase = change_in_profits.index(change)
    elif change == greatest_decrease:
        #saves the index to a new variable
        index_greatest_decrease = change_in_profits.index(change)

#change_in_profits is the same length as new_profits_and_losses - so the indicies are the same
#finding the pair in new_profits_and_losses that matches the index of greatest_increase and greatest_decrease
value_after_greatest_increase = new_profits_and_losses[index_greatest_increase][1]
value_after_greatest_decrease = new_profits_and_losses[index_greatest_decrease][1]

#going through the csv file to pull the change information
with open (pybank_csv, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     #pulls header row out
     csv_header = next(csvreader)
     #for each row in the csv file
     for row in csvreader:
         #looks for the value in the second column that matches the value after greatest_increase
         if row[1] == value_after_greatest_increase:
             #saves the row's date value to a variable
             date_greatest_increase = row[0]
         #looks for the value in the second column that matches the value after greatest_decrease
         elif row[1] == value_after_greatest_decrease:
             #saves the row's date value to a variable
             date_greatest_decrease = row[0]

#printing the required text to the terminal
print("Financial Analysis")
print("-------------------------------")
#print total months as rows
print(f"Total Months: {row_count}")
#prints the net profits
print(f"Total: ${total_profits}")
#prints the average change in profits/Losses, rounded to 2 decimal places (since we're dealing with money)
print(f"Average Change: ${round(avg_change, 2)}")
#prints the greatest increase in profits
print(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})")
#prints the greatest decrease in profits
print(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})")

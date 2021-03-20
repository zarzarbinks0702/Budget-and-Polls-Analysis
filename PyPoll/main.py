import os
import csv

#link to the csv data file for pybank project
csvpath = os.path.join("Resources", "election_data.csv")

#set initial value for row count, used to find the total number of votes cast
row_count = 0

#open csv data file for pybank project and make it readable
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #pulls header row out
    csv_header = next(csvreader)
    #for each row in the csv file
    for row in csvreader:
        #adds one to the row count for each row
        row_count += 1

#prints the total number of votes cast
print(f"Total Votes Cast: {row_count}")

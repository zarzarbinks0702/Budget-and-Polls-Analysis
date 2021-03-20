import os
import csv

#link to the csv data file for pybank project
csvpath = os.path.join("Resources", "election_data.csv")

#open csv data file for pybank project and make it readable
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #pulls header row out
    csv_header = next(csvreader)

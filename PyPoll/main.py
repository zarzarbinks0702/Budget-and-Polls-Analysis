import os
import csv

#link to the csv data file for pybank project
csvpath = os.path.join("Resources", "election_data.csv")

#set initial value for row count, used to find the total number of votes cast
vote_count = 0
#set initial value for the candidate list
candidates = []

#open csv data file for pybank project and make it readable
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #pulls header row out
    csv_header = next(csvreader)
    #for each row in the csv file
    for row in csvreader:
        #adds one to the vote count for each row (one row = one vote)
        vote_count += 1
        #checks the value of the 3rd column is in the candidates list
        if row[2] in candidates:
            #does nothing if the name is already in the list
            pass
        #if the name is not in the candidates list
        else:
            #adds the name to the candidates list
            candidates.append(row[2])
        #function for determining total votes and percentage of votes won by each candidate - takes the index of the candidates list as a parameter
        def vote_count(candidate_index)
            #count how many times a candidate's name appears in the 3rd column
            candidate_votes = row[2].count(candidates[candidate_index])
            #uses vote_count and candidate_votes to find the percentage of votes
            percentage_votes = int(candidate_votes) / int(vote_count) * 100
            #prints the information to the console
            print(f"{candidates[candidate_index]}: {round(percentage_votes, 3)}% ({candidate_votes})")

#prints the total number of votes cast
print(f"Total Votes: {vote_count}")

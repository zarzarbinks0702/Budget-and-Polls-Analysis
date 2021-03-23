import os
import csv

#link to the csv data file for pybank project
csvpath = os.path.join("Resources", "election_data.csv")

#set initial value for row count, used to find the total number of votes cast
total_vote_count = 0
#set initial value for the candidate list
candidates = []
#stores the third column as a list
all_vote_names = []
#open csv data file for pybank project and make it readable
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #pulls header row out
    csv_header = next(csvreader)
    #for each row in the csv file
    for row in csvreader:
        #adds one to the vote count for each row (one row = one vote)
        total_vote_count += 1
        #checks the value of the 3rd column is in the candidates list
        if row[2] in candidates:
            #does nothing if the name is already in the list
            pass
        #if the name is not in the candidates list
        else:
            #adds the name to the candidates list
            candidates.append(row[2])
        #adds each item in the third column to the all_vote_names list
        all_vote_names.append(row[2])
    #function for determining total votes and percentage of votes won by each candidate - takes the index of the candidates list as a parameter
    def vote_count(candidate_index):
        #count how many times a candidate's name appears in the 3rd column (stored in the all_vote_names list)
        candidate_votes = all_vote_names.count(candidates[candidate_index])
        #uses vote_count and candidate_votes to find the percentage of votes
        percentage_votes = candidate_votes / total_vote_count * 100
        #prints the information to the console
        print(f"{candidates[candidate_index]}: {round(percentage_votes, 3)}% ({candidate_votes})")

#prints the total number of votes cast
print(f"Total Votes: {total_vote_count}")
#prints the vote_count function for each candidate in the candidates list
for each in range(len(candidates)):
    print(vote_count(each))

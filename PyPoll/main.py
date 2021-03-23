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
#stores total individual vote counts in one list
individual_vote_count = []

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
        #appends candidate_votes number to individual_vote_count list
        individual_vote_count.append(candidate_votes)
        #uses vote_count and candidate_votes to find the percentage of votes
        percentage_votes = candidate_votes / total_vote_count * 100
        #prints the information to the console
        return f"{candidates[candidate_index]}: {round(percentage_votes, 3)}% ({candidate_votes})"

print("Election Results")
print("------------------------------")
#prints the total number of votes cast
print(f"Total Votes: {total_vote_count}")
print("------------------------------")
#prints the vote_count function for each candidate in the candidates list
for each in range(len(candidates)):
    print(vote_count(each))
print("------------------------------")
#since the vote_count function is based on the candidates list, the index of the candidate in cndidates should be the same as the index of their vote vcount in individual_vote_count
#zip the individual_vote_count and candidate lists together in that order so that the sort function sorts it by the vote count, not alphabetically
candidates_and_votes = list(zip(individual_vote_count, candidates))
#sorts candidates_and_votes so that the
candidates_and_votes.sort()
#prints the last item in the last object of the new, sorted list, which is the winner's name
print(f"Winner: {candidates_and_votes[-1][1]}")
print("------------------------------")

#create a new txt document to print the results above to
with open ('Analysis\pypoll_results.txt', 'w') as txtfile:
    txtfile.write(
    "Election Results\n"
    "------------------------------\n"
    f"Total Votes: {total_vote_count}\n"
    "------------------------------\n"
    #for this case, we know there are 4 candidates
    f"{vote_count(0)}\n"
    f"{vote_count(1)}\n"
    f"{vote_count(2)}\n"
    f"{vote_count(3)}\n"
    "------------------------------\n"
    f"Winner: {candidates_and_votes[-1][1]}\n"
    "------------------------------\n")

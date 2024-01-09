#import libraries. 
import os
import csv

#set file path for input/output
csvpath = "../Resources/election_data.csv"
election_data = os.path.join("C:\\Users\\artsy\\OneDrive\\Desktop\\python-challenge-repo\\python-challenge\\Resources\\election_data.csv")
file_to_output = "analysis_pypoll.txt"

#Initialize Variables
total_votes = 0
candidate_set = set()
candidate_votes = {}

#Open and read the CSV file.
with open(csvpath, newline="", encoding="utf-8") as csvfile:#I still don't know why utf-8 makes it work?
    csv_reader = csv.reader(csvfile,delimiter=",")
    next(csv_reader) #Skip the header row. 
    #calculate the number of votes. 
    for row in csv_reader:
        total_votes += 1
        #A complete list of candidates who received votes
        candidate_name = row[2]
        if candidate_name not in candidate_set:
            candidate_set.add(candidate_name)
            candidate_votes[candidate_name] = 0
        #Candadite's vote tally 
        candidate_votes[candidate_name] += 1
       
#calculate the percentage of votes each candidate won.
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

#who won? Lets see shall we?
winner = max(candidate_votes, key=candidate_votes.get)

print(f"Total votes: {total_votes}")
print("list of canidates who received votes:")
for candidate in candidate_set:
    print(candidate)
for candidate, votes in candidate_votes.items():
    percentage = percentage_votes[candidate]
    print(f"{candidate}: {percentage: .3f}% ({votes} votes)")
print(f"Winner: {winner}")

#Export
with open(file_to_output, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total votes: {total_votes}\n")
    output_file.write("List of candidates who received votes:\n")
    for candidate in candidate_set:
        output_file.write(f"{candidate}\n")
    for candidate, votes in candidate_votes.items():
        percentage = percentage_votes[candidate]
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes} votes)\n")
    output_file.write(f"Winner: {winner}\n")

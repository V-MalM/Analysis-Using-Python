# Written By : Vasantha M Mutyala
# Date : 5/30/2021
# Reads a csv file 'election_data.csv' from Resources folder, analyzes data , performs calculations , creates an out put text file 'election_results.txt' in 'analysis' folder and writes election results to it.

# Dependencies
import os
import csv

# Path to collect data from the 'Resources' folder
# 'election_data.csv'
source_file = os.path.join(os.getcwd(),'Resources','election_data.csv')

candidate_votes = [] # 2. A complete list of candidates who received votes
candidate_list_unique = set() # To create a list of unique candidates

with open(source_file,'r', encoding="utf8") as csvsourcefile:

    # Reads the data from csv file and creates a dictonary preserving the header with each header filed as a key
    csvsourcedata = csv.DictReader(csvsourcefile,delimiter=",")
    for row in csvsourcedata:
        candidate_votes.append(row['Candidate'])
        candidate_list_unique.add(row['Candidate'])  

candidate_vote_count_dict = {} #dictionary to store each candidate name and their total vote count. This can be done using tuples aswell. but i am using a dictonary because I used tuples in PyBank

for i in candidate_list_unique :
    candidate_vote_count_dict[i] = candidate_votes.count(i)

# sorting the dictonary in descending order of candidate's number of votes. Dictonary doesn't have a provision to be sorted but dictonary has items() method that returns a view of list of tuples, each tuple having key and value of each pair in a dictionary, that can be sorted. 

d_sorted = sorted(candidate_vote_count_dict.items(),key=lambda x:x[1],reverse=True)

# 1. The total number of votes cast
Total_Votes = len(candidate_votes)

res_Output_str = ""
per_votes = 0

# looping through the sorted list to display candidates and their votes starting with the candidate with highest number of votes
for i in d_sorted:

    # Calculating percentage of votes for each candidate
    per_votes = (i[1]/Total_Votes)*100

    # 3.1 Creating an output string that shows candidate name and the percentage of votes each candidate won
    # 3.2 The out put string also has the total number of votes each candidate won
    res_Output_str += i[0] + ": " + "{:.3f}".format(per_votes) + "% (" + str(i[1]) + ')\n'

# The winner of the election based on popular vote. it is the first value of the first tuple from sorted list 
winner_str = 'Winner: ' +  d_sorted[0][0] +'\n'

# Result Output 
Output_str = ('\n')
Output_str += 'Election Results'+'\n'
Output_str += '-------------------------' +'\n'
Output_str += 'Total Votes: ' + str(Total_Votes)+'\n'
Output_str += '-------------------------' +'\n'
Output_str += res_Output_str
Output_str += '-------------------------' + '\n'
Output_str += winner_str
Output_str += '-------------------------' +'\n'
Output_str += ('\n')

# Print the election result to the terminal
print(Output_str)

# Path to Output file in the 'analysis' folder
# 'election_results.txt'
output_file = os.path.join(os.getcwd(),'analysis','election_results.txt') 

# Write results to output file
with open (output_file, mode="w") as txtfile:
    txtfile.write(Output_str)
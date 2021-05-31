# Written By : Vasantha M Mutyala
# Date : 5/30/2021
# Reads a csv file 'election_data.csv' from Resources folder, analyzes data , performs calculations , creates an out put text file 'election_results.txt' in 'analysis' folder and writes election results to it.

# Dependencies
import os
import csv

#*******************************************FUNCTIONS*******************************************

# Funtion that accepts csv sourcefile, reads data and writes to a list and a set , returns them for further analysis
def readFromCsv(srcFile):
    candidateVotes = [] # 2. A complete list of candidates who received votes
    candidateListUnique = set() # To create a list of unique candidates
    with open(srcFile,'r', encoding="utf8") as csvsourcefile:

        # Reads the data from csv file and creates a dictonary preserving the header with each header filed as a key
        csvsourcedata = csv.DictReader(csvsourcefile,delimiter=",")
        for row in csvsourcedata:
            candidateVotes.append(row['Candidate'])
            candidateListUnique.add(row['Candidate'])  

    return  candidateVotes, candidateListUnique     

# Function the accepts candidatevotes list candidateListUnique set for further analysis and output 
def analyzeAndWrite(candVotes, candUniqueList):
    candidate_vote_count_dict = {} #dictionary to store each candidate name and their total vote count. This can be done using tuples aswell. but i am using a dictonary because I used tuples in PyBank

    for i in candUniqueList :
        candidate_vote_count_dict[i] = candVotes.count(i)

    # sorting the dictonary in descending order of candidate's number of votes. Dictonary doesn't have a provision to be sorted but dictonary has items() method that returns a view of list of tuples, each tuple having key and value of each pair in a dictionary, that can be sorted. I used sorted() function here to sort.

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
    try: 
        with open (output_file, mode="w") as txtfile:
            txtfile.write(Output_str)
    except FileNotFoundError :  
        print ("\n********OUTPUT FOLDER NOT FOUND. Results to output file cannot be written********\n")  
        print ("Output folder not found or the path is incorrect. Please make sure your working \ndirectory is PyPoll and it has 'analysis' folder.\n") 
        print ("**********************************************************************************\n")    
        exit       

#*******************************************END OF FUNCTIONS*******************************************


# Path to collect data from the 'Resources' folder
# 'election_data.csv'
source_file = os.path.join(os.getcwd(),'Resources','election_data.csv')

candidate_votes = [] # 2. A complete list of candidates who received votes
candidate_list_unique = set() # To create a list of unique candidates

# Error handling if the file is not found or path is incorrect, it will message the user. 
try:
    # calles function  readFromCsv and passes the source_file
    candidate_votes, candidate_list_unique = readFromCsv(source_file)

# if the file is not found or path is incorrect, it will message the user. 
except FileNotFoundError :  
    print ("\n******************************** FILE NOT FOUND ********************************\n")  
    print ("File not found or the path is incorrect. Please make sure your working directory\nis PyPoll and it has both 'Resources' and 'analysis' folders. \nAlso make sure file 'election_data.csv' is present in 'Resources' folder\n") 
    print ("*********************************************************************************\n")    
    exit   

# Any other error 
except:
    print ("\n******************************** Unknown Error ********************************\n")  
    print ("Error Occured. Plase contact the IT department\n") 
    print ("*********************************************************************************\n")    
    exit  

# if no errors, calls the function to analyse and generate output    
else:
    # calles function  analyzeAndWrite and passes the candidate_votes, candidate_list_unique returned by previous function
    analyzeAndWrite(candidate_votes, candidate_list_unique)

      
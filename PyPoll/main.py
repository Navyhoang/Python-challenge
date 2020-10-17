import os
import csv

#Open reosurces file
datafile_csv = os.path.join("PyPoll","Resources", "election_data.csv")

#-------------------------------------------------------------------------
# Total number of votes casted
# List of unique candidates
# Approach: Iterative loop
#-------------------------------------------------------------------------

#Empty parametersd li
total_voters_count = 0
Candidates_list = []

with open(datafile_csv,'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
#skip the header row
    header = next(csv_reader)

    #for row in csv_reader:
    for row in csv_reader:
        total_voters_count += 1
        
        #list of candidates
        if str(row[2]) not in Candidates_list:
            Candidates_list.append(row[2])

#-------------------------------------------------------------------------
# Number of votes each candidate won
# Approach: Iterative loop and Dictionary
#-------------------------------------------------------------------------

# Create a counter
voters_count_i = 0 

#Create an empty dictionary
new_dict = {}

#Loop through each candidate name in the Candidates_list created above
for i in range(len(Candidates_list)):

    candidate_i = Candidates_list[i]

    # Reset counter for the next candidate
    voters_count_i = 0

    #Open source file
    with open(datafile_csv,'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        #Skip header
        header = next(csv_reader)

        #Loop through each row, count 1 if name match candidate name in the Candidates_list
        for row in csv_reader:
            if str(row[2]) == candidate_i:
                voters_count_i += 1

    # Once done looping through all rows, add candidate name and vote count to dictionary 
    new_dict[candidate_i] = voters_count_i

    # Then go to the next candidate
#-------------------------------------------------------------------------
# The winner of election based on percentage of votes won
# Approach: Find largest value in Dictionary and its associated key
#-------------------------------------------------------------------------

#Find largest value in the dictionary and return it's key
max_key = max(new_dict, key=new_dict.get)

# Create the output parameter
output = (f"Election Results\n"
          f"-------------------------------------------\n"
          f"Total Votes: {total_voters_count}\n"
          f"-------------------------------------------\n"
          f"{list(new_dict.keys())[0]}: {round(new_dict[list(new_dict.keys())[0]]/total_voters_count*100,4)}% ({new_dict[list(new_dict.keys())[0]]})\n"
          f"{list(new_dict.keys())[1]}: {round(new_dict[list(new_dict.keys())[1]]/total_voters_count*100,4)}% ({new_dict[list(new_dict.keys())[1]]})\n"
          f"{list(new_dict.keys())[2]}: {round(new_dict[list(new_dict.keys())[2]]/total_voters_count*100,4)}% ({new_dict[list(new_dict.keys())[2]]})\n"
          f"{list(new_dict.keys())[3]}: {round(new_dict[list(new_dict.keys())[3]]/total_voters_count*100,4)}% ({new_dict[list(new_dict.keys())[3]]})\n"
          f"-------------------------------------------\n"
          f"Winner:{max_key}\n"
          f"-------------------------------------------\n")
    
#print to terminal
print(output)

#print to a csv file
# Open an output file and write results
Analysis_file = os.path.join("PyPoll","Analysis","Analysis_final.csv")

with open(Analysis_file,'w') as outputfile:
    
    outputfile.write(output)
    
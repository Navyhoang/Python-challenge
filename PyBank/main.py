#Open the budget_data file to read and calculate:
#Open a text file to write to:
    #Total number of months (how many rows), Skip the header
    #Net profit/loss (sum of column B), skip the header
    #Average of the profit/loss (average of column B), skip the header
    # Find the greatest increase in profits (max of column B) then print the entire row
    # Find the greatest decreasse in losses (min of column B) then print the entire column
    
import os
import csv

#Open reosurces file
datafile_csv = os.path.join("PyBank","Resources", "budget_data.csv")

#--------------------------------------------------------------------------------------------------
# Total number of months
#--------------------------------------------------------------------------------------------------

monthlist = []

#open the budget_data.csv file to read
with open(datafile_csv, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    csv_header = next(csvfile, None)

    #Loop through each row, check if each cell in column 1 is not empty,
    #then add to the list, then count number of months in the list
    for row in csv_reader:
        if str(row[0]) != " ":

            monthlist.append(row[0])
            monthcount = len(monthlist)

            #print(monthcount)

           
                        
#--------------------------------------------------------------------------------------------------
# Net profit/loss
#--------------------------------------------------------------------------------------------------

    netlist = []
    net = 0

#Loop through each row in range monthcound, +1 because the last item is excluded when using range
    for i in range(monthcount + 1):

        #add the value to the list
        netlist.append(int(row[1]))

        #then sum all values in the list
        net = sum(netlist)



#--------------------------------------------------------------------------------------------------
#Average of the profit/loss (average of column B), skip the header
#--------------------------------------------------------------------------------------------------

# Python program to get average of a list 
def Average(netlist): 
    return sum(netlist) / len(netlist) 
  
# Find average 
average = Average(netlist) 
  


#--------------------------------------------------------------------------------------------------
#Find the greatest increase in profits (max of column B) then print the entire row
#--------------------------------------------------------------------------------------------------

greatest_increase = max(netlist)

#--------------------------------------------------------------------------------------------------
#Find the greatest decreasse in losses (min of column B) then print the entire column
#--------------------------------------------------------------------------------------------------

greatest_decrease = min(netlist)



# Open an output file and write results
Analysis_file = os.path.join("Analysis_final.csv")

with open(Analysis_file,'w', newline="") as outputfile:
    writer = csv.writer(outputfile)
    print(f"There are total of {monthcount} months in the list")
    print(f"The net profit/ lost is {netprofit} dollars")
    print("Average of the list =", round(average, 2))
    
    for i in range(1,monthcount + 1):

        if row[1] == greatest_increase:
            print(f"The greast profit occured on {row[0]} and net profit of {row[1]}")
            writer.writerow(["Month","Profit/Loss"])
            writer.writerrows(i)

        elif row[1] == greatest_decrease:
            print(f" The greast loss occured on {row[0]} and net loss of {row[1]}")
            writer.writerow(["Month","Profit/Loss"])
            writer.writerrows(i)


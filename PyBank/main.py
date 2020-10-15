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
datafile_csv = os.path.join("Resources", "budget_data.csv")

#-------------------------------------------------------------------------
# Month count, Net Profit/Loss
# Approach: Append to List then find length and Sum 
#-------------------------------------------------------------------------

# Create empty lists to hold values in column 1, column 2
monthlist = []
netlist = []

# Create empty lists to hold the difference in profit between the current month and previous month
net_change_list = []
net_change_month = []

#Set arbitrary arrays for comparison loop later
# greatest_increase = [Date of greatest increase, greatest increase]
greatest_increase = ["", 0]

# greatest_increase = [Date of greatest decrease, greatest decrease]
greatest_decrease = ["", 10000000000000000000]


#open the budget_data.csv file to read
with open(datafile_csv, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    header = next(csv_reader)

            
    #Loop through each row, check if each cell in column 1 is not empty,
    for row in csv_reader:

        #then add all values in column 1 to the monthlist
        monthlist.append(row[0])
            
        # then count number of months in the monthlist
        monthcount = len(monthlist)
            
        #add the values in column 2 to the netlist
        netlist.append(int(row[1]))

        #then sum all values in the netlist
        net = sum(netlist)
                       
        #Format numbers to currency
        net_formated = "${:}".format(net)   
              
 #open the budget_data.csv file to read
with open(datafile_csv, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    header = next(csv_reader)
    
    #Set first row
    firstrow = next (csv_reader)
    
    # Extract the profit value of the first row
    previous_net = int(firstrow[1])
       
    for row in csv_reader:
                
        # Subtract previous month's profit from the current month's profit
        netchange = int(row[1]) - previous_net        
               
        # Add the netchange of the current month to the net_change_list
        net_change_list += [netchange]
        
        # Add the date of the current month to the net_change_month
        net_change_month += [row[0]]
    
        # Compare each row to the arbitrary arrays adn replace with the larger value and date
        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = netchange
            
        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange
            
        # Then reset the previous_net to current month
        previous_net = int(row[1])
        
        greatest_increase_formated = "${:}".format(greatest_increase[1])
        greatest_increase_date = (greatest_increase[0]) 
            
    
        greatest_decrease_formated = "${:}".format(greatest_decrease[1]) 
        greatest_decrease_date = (greatest_decrease[0])


#------------------------------------------------------------------------
# Average Net Change
# Approach: Use Function 
#------------------------------------------------------------------------

    #Use Functions to find Average
    def Average(netlist): 
        return sum(net_change_list) / len(net_change_list) 
    
    # Call the defined function
    average = Average(netlist) 

    #round average
    average_rounded = round(average)

    #average_formated
    average_formated = "${:}".format(average_rounded)

#Create an output parameter
output = (f"Financial Analysis \n"
          f"--------------------------------------------------------------------------------\n"
         f"There are total of {monthcount} months in the list \n"
         f"Net profit/ lost is {net_formated} \n"
         f"Average net change is {average_formated} \n"
         f"The greatest increase in profit is {greatest_increase_formated} on {greatest_increase_date} \n"
         f"The greatest decrease in profit is {greatest_decrease_formated} on {greatest_decrease_date}")

#print to terminal
print(output)

#print to a csv file
# Open an output file and write results
Analysis_file = os.path.join("Analysis","Analysis_final.csv")

with open(Analysis_file,'w') as outputfile:
    
    outputfile.write(output)
    
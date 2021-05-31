# Written By : Vasantha M Mutyala
# Date : 5/30/2021
# Reads a csv file 'budget_data.csv' from Resources folder, analyzes data , performs calculations , creates an out put text file 'budget_analysis.txt' in 'analysis' folder and writes summary of analysis to it.

# Dependencies
import os
import csv

#  imports a module datetime to work with dates as date objects.
from datetime import datetime


#*******************************************FUNCTIONS*******************************************

# Funtion that accepts csv sourcefile, reads data and writes to a list, returns it for further analysis
def readFromCsv(srcFile):
    # local variable for list into which the source data will be read in to a list of tuples.
    ProfitLossList = []   
    with open(srcFile,'r', encoding="utf8") as csvsourcefile:
         # Reads the data from csv file and creates a dictonary preserving the header with each header filed as a key
        csvsourcedata = csv.DictReader(csvsourcefile,delimiter=",")
        for row in csvsourcedata:
        
            #coverting Date column that is in str format to datetime so we can sort the data by date  
            datecol = datetime.strptime(row['Date'],'%b-%Y')         
            
            #adding data in to the list as tuples each tuple containing date and corresponding profilt/loss value
            ProfitLossList.append((datecol, float(row['Profit/Losses']))) 
    return(ProfitLossList)        

# Function that accepts ProfitLossList (list of tuples) for analysis, performs calculations and generates output 
def analyzeAndWrite(Profit_Loss_List):
    # sort() method sorts and rearranges the list of tuples in order of date
    # using lamda function here
    Profit_Loss_List.sort(key = lambda x:x[0])  
    # The list is now ready for further calculations

    # 1. The total number of months included in the dataset
    total_number_of_months  = len(Profit_Loss_List)

    # This calculates rate of change for each month and saves it into a list of tuples with date and change in profit/loss. Inside the loop it also creates list just to store changes in profit/loss. This is to get min and max without having to use list comprehensions that will run a for loop each time an agggregate function is called

    monthly_change_list_tbl_with_date = []
    list_of_monthly_changes  = []
    prev = 0
    rec_count = 0
    total_Profit_Losses = 0
    total_change_for_all_months = 0
    average_change = 0
    for i in Profit_Loss_List:
        monthly_change = 0    
        curr_val = i[1]

        # 2. Calculates the net total amount of "Profit/Losses" over the entire period
        total_Profit_Losses += curr_val
        if prev != 0:
            monthly_change = curr_val - prev
            rec_count += 1
        monthly_change_list_tbl_with_date.append((i[0], monthly_change)) 
        list_of_monthly_changes.append(monthly_change)

        # 3.1 Calculates the changes in "Profit/Losses" over the entire period
        total_change_for_all_months+= monthly_change
        prev = i[1]
            
        
    # 3.2 Calculate the average of the changes in "Profit/Losses" over the entire period
    if rec_count > 0:
        average_change = round(total_change_for_all_months/rec_count,2)

    # 4.1 gets and stores greatest increase to this variable
    Greatest_Increase_in_Profits  = max(list_of_monthly_changes)

    # 5.1 gets and stores greatest decrease to this variable
    Greatest_Decrease_in_Profits  = min(list_of_monthly_changes)

        
    # Formatting floating values for display 
    total_Profit_Losses = "{:.0f}".format(total_Profit_Losses)
    Greatest_Increase_in_Profits_formmatted = "{:.0f}".format(Greatest_Increase_in_Profits)
    Greatest_Decrease_in_Profits_formmatted = "{:.0f}".format(Greatest_Decrease_in_Profits)

    # The out put string for greatest increase (date and amount) over the entire period
    GIIP_Str = ""

    # The out put string for greatest decrease (date and amount) over the entire period
    GDIP_Str = ""

    # Loops throgh the monthly_change_list_tbl_with_date . This will make sure that if there is more than one month with exact rate of change values , it displays those as well 
    # 4.2. fetches the corresponding date for greatest increase, formats it to string for display and adds to output string
    # 5.2. fetches the corresponding date for greatest decrease, formats it to string for display and adds to output string

    for i in monthly_change_list_tbl_with_date:
        if i[1] == Greatest_Increase_in_Profits :
            GIIPDate = i[0]
            GIIPDate = GIIPDate.strftime('%b-%Y') 
            GIIP_Str += 'Greatest Increase in Profits: ' + GIIPDate + ' $(' + str(Greatest_Increase_in_Profits_formmatted) +')'+ ('\n')

        if i[1] == Greatest_Decrease_in_Profits :
            GDIPDate = i[0]
            GDIPDate = GDIPDate.strftime('%b-%Y')
            GDIP_Str += 'Greatest Decrease in Losses: ' + GDIPDate + ' $(' + str(Greatest_Decrease_in_Profits_formmatted) +')'+ ('\n')

    # Analysis Output 
    Output_str = ('\n')
    Output_str = Output_str + 'Financial Analysis'+ ('\n')
    Output_str = Output_str + '----------------------------'+ ('\n')
    Output_str = Output_str + 'Total Months:' + str(total_number_of_months)+ ('\n')
    Output_str = Output_str + 'Total: $' + str(total_Profit_Losses)+ ('\n')
    Output_str = Output_str + 'Average  Change: $' +  str(average_change)+ ('\n')
    Output_str = Output_str + GIIP_Str
    Output_str = Output_str + GDIP_Str
    Output_str = Output_str + ('\n')

    # Print the analysis to the terminal
    print(Output_str)

    # Path to Output file in the 'analysis' folder
    # 'budget_analysis.txt'
    output_file = os.path.join(os.getcwd(),'analysis','budget_analysis.txt') 

    # Write results to output file
    try: 
        with open (output_file, mode="w", newline='') as txtfile:
            txtfile.write(Output_str)
    except FileNotFoundError :  
        print ("\n********OUTPUT FOLDER NOT FOUND. Results to output file cannot be written********\n")  
        print ("Output folder not found or the path is incorrect. Please make sure your working \ndirectory is PyBank and it has 'analysis' folder.\n") 
        print ("**********************************************************************************\n")    
        exit 

#*******************************************END OF FUNCTIONS*******************************************


# Path to collect data from the 'Resources' folder
# 'budget_data.csv'
source_file = os.path.join(os.getcwd(),'Resources','budget_data.csv') 

# list into which the source data will be read in to a list of tuples.
PftLssLst = []   

# Error handling if the file is not found or path is incorrect, it will message the user. 
try:
    PftLssLst = readFromCsv(source_file)                                            
    
# if the file is not found or path is incorrect, it will message the user. 
except FileNotFoundError :  
    print ("\n******************************** FILE NOT FOUND ********************************\n")  
    print ("File not found or the path is incorrect. Please make sure your working directory\nis PyBank and it has both 'Resources' and 'analysis' folders. \nAlso make sure file 'budget_data.csv' is present in 'Resources' folder\n") 
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
    # calles function  analyzeAndWrite and passes the PftLssLst returned by previous function
    analyzeAndWrite(PftLssLst)


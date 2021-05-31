### Python-Challenge
#### Project Description --> This python project has two tasks:
### 1. PyBank 
* Created a Python script for analyzing the financial records of a company from a set of financial data 'budget_data.csv' that is composed of two columns: Date and Profit/Losses.The script analyzes the records to calculate each of the following:
    * The total number of months included in the dataset
    * The net total amount of "Profit/Losses" over the entire period
    * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in losses (date and amount) over the entire period
    * Analysis looks similar to the one below:
      <br><img src="https://user-images.githubusercontent.com/81383838/120222188-2a958880-c205-11eb-841a-8548d1d0f7f6.jpg" width="500">
      
#### Resources
   * Folder PyBank : This folder contains two folders 
   		* 'Resources': Contains the financial data 'budget_data.csv'
   		* 'analysis' : Empty folder to which the output text file with analysis, will be written.
   * Python file 'main.py' that has python script for analyzing the financial data stored in 'Resources\budget_data.csv'

#### Key notes
   * Used csv.DictReader that reads the data from csv file and creates a dictonary preserving the header with each header filed as a key.
   * Used 'from datetime import datetime' that imports a module 'datetime' to work with dates as date objects.
   * Used tuples to work with data for further analysis.
   * Used sort() method to sorts and rearranges the list of tuples in order of date
   * Used lamda function to sort
 
#### Execution:
  * The script is in the file main.py which can be located in the folder PyBank.
  * Using PyBank as the working folder, run 'main.py'.
  * The file has detailed comments expaling each step
  
#### Results:
   * The following analysis is printed to the terminal and the same result is written to output text file 'analysis/budget_analysis.txt'
   <br><img src="https://user-images.githubusercontent.com/81383838/120222188-2a958880-c205-11eb-841a-8548d1d0f7f6.jpg" width="500">

#### Important: Run 'main.py' from PyBank as current working direcory
###### eRRORS !!!! What ERRORS ????
* Handled 'Filenotfound' errors in case the script cannot find the source or destination folders/file
* Made sure 'ZeroDivisionError' doesn't occur
* REST ASSURED, The code runs error free. Just Follow these detailed instructions ....



### Python-Challenge
#### Project Description --> This python project has two tasks: 
##### PyBank and PyPoll , both read an individual csv file, analyze data, perform calculations, print summary of analysis to screen and also create an output text file  and write summary of analysis to it. 
* I explored Lists, Dictonaries, Tuples and sets, error handling using 'try..except..else..'
* In PyBank, used TUPLE where required. Also used datetime module , lamda function and sort() method to sort data.
* In PyPoll, used SET where required. Used lambda funtion along with python sorted() function. 
    * Instead of checking candidates name in a for loop to create a unique list of candidates, i used a set.

##### Explained in detail
### 1. PyBank 
* Created a Python script for analyzing the financial records of a company from a set of financial data 'budget_data.csv' that is composed of two columns: Date and Profit/Losses.The script analyzes the records to calculate each of the following:

    * The total number of months included in the dataset
    * The net total amount of "Profit/Losses" over the entire period
    * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in losses (date and amount) over the entire period
    * Analysis looks similar to the one below:
      <br><img src="https://user-images.githubusercontent.com/81383838/120222188-2a958880-c205-11eb-841a-8548d1d0f7f6.jpg" width="500">
      
#### Resources:
   * Folder PyBank : This folder contains two folders 
   		* 'Resources': Contains the financial data 'budget_data.csv'
   		* 'analysis' : Empty folder to which the output text file with analysis, will be written.
   		* Python file 'main.py' that has python script for analyzing the financial data stored in 'Resources/budget_data.csv'

#### Key notes:
   * Used csv.DictReader that reads the data from csv file and creates a dictonary preserving the header with each header field as a key.
   * Used 'from datetime import datetime' that imports a module 'datetime' to work with dates as date objects.
   * Used tuples to work with data for further analysis.
   * Used sort() method to sort and rearrange the list of tuples in order of date
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

### 2. PyPoll 
* Created a Python script for helping a small, rural town modernize its vote counting process by analyzing poll data in 'election_data.csv' that is composed of three columns: Voter ID, County, and Candidate.This script analyzes the votes and calculates each of the following:

    * The total number of votes cast
    * A complete list of candidates who received votes
    * The percentage of votes each candidate won
    * The total number of votes each candidate won
    * The winner of the election based on popular vote.
    * Analysis looks similar to the one below:
      <br><br><img src="https://user-images.githubusercontent.com/81383838/120231311-bbc12b00-c216-11eb-9b01-50ccd9258b42.jpg" width="200">
      
#### Resources:
   * Folder PyPoll   : This folder contains two folders 
   		* 'Resources': Contains poll data 'election_data.csv'
   		* 'analysis' : Empty folder to which the output text file with analysis, will be written.
   		* Python file 'main.py' that has python script for analyzing the election_data data stored in 'Resources/election_data.csv'

#### Key notes:
   * Used csv.DictReader that reads the data from csv file and creates a dictonary preserving the header with each header field as a key.
   * Used SET to create a unique list of candidates.
   * Used lamda function
   * Used sorted() function to sort and rearrange the date 
 
#### Execution:
  * The script is in the file main.py which can be located in the folder PyPoll.
  * Using PyPoll as the working folder, run 'main.py'.
  * The file has detailed comments expaling each step
  
#### Results:
   * The following analysis is printed to the terminal and the same result is written to output text file 'analysis/election_results.txt'
   <br><br><img src="https://user-images.githubusercontent.com/81383838/120231311-bbc12b00-c216-11eb-9b01-50ccd9258b42.jpg" width="200">

#### Important: Run 'main.py' from PyPoll as current working direcory
###### eRRORS !!!! What ERRORS ????
* Handled 'Filenotfound' errors in case the script cannot find the source or destination folders/file
* Made sure 'ZeroDivisionError' doesn't occur
* REST ASSURED, The code runs error free. Just Follow these detailed instructions ....


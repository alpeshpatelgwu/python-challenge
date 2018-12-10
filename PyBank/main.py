import os
import csv
import pandas as pd 

#electionpath = os.path.join('..', 'resources', 'election_data.csv')

print("This is HW Assignment #3")
print("")

# Create a variable that holds the import of the Budget_Data CSV File
# budgetpath = os.path.join('..', 'resources', 'budget_data.csv')
budgetpath = "C:\\Users\\aipat\\python-challenge\\resources\\budget_data.csv"

months = []
total = []

with open(budgetpath, 'r') as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=",")
    budgetheader = next(budgetreader)
    
    decrease = 0
    increase = 0

    
    #this will iterate through each row of the csv file and read it
    #this for loop will continue to loop through the csvfile till 
    #it reaches the end
    # === What do you want to do in this loop? ===
    for row in budgetreader:
        #print(f'{row[0]} {row[1]}')
        #print(f'{row[1]}')
        
        #this will store the values of each column in either months list or total list

        months.append(row[0])
        total.append(row[1])
        


     zip(months, total)
    
    
        
    totalsum = sum(int(x) for x in total)
    avgchange = int(totalsum / len(total))



print("")
print(f'There are a total of {len(months)} months')
print("")
print(f'The total profit/loss margin is ${totalsum}')
print(f'The average is ${avgchange}')
print("This is the end")




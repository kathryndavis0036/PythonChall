#PyPoll
# Modules
import os
import csv

import pandas as pd

# Set path for file
csvpath = os.path.join("Users","kathryndavis","Downloads","Starter_Code 5","PyPoll","Resources","election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    # print(f"Header: {csv_header}")

df = pd.read_csv("election_data.csv") 

# block 1 - simple stats
sum1 = df['Total'].sum()
count1 = df['Charles Casper Stockham'].count()
count2 = df['Diana DeGette'].count()
count3 = df['Raymon Anthony Doane'].count()

# print block 1
print('Election Results')
print('----------------------------')
print('Average Change: ' + str(mean1))
print('Total Votes: ' + str(sum1))
print('----------------------------')
print('Greatest Increase in Profits: ' + str(max1))
print('Greatest Decrease in Profits: ' + str(min1))
print('----------------------------')
print('Winnter: ' + str(count2))
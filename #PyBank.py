#PyBank
# Modules
import os
import csv

import pandas as pd

# Set path for file
csvpath = os.path.join("Users","kathryndavis","Downloads","Starter_Code 2","PyBank","Resources","budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    # print(f"Header: {csv_header}")

df = pd.read_csv("budget_data.csv") 

# block 1 - simple stats
mean1 = df['Profit/Losses'].mean()
sum1 = df['Profit/Losses'].sum()
max1 = df['Profit/Losses'].max()
min1 = df['Profit/Losses'].min()
count1 = df['Date'].count()

# print block 1
print('Financial Analysis')
print('----------------------------')
print('Average Change: ' + str(mean1))
print('Total: ' + str(sum1))
print('Greatest Increase in Profits: ' + str(max1))
print('Greatest Decrease in Profits: ' + str(min1))
print('Months: ' + str(count1))
import os
import csv

csvpath = "../Resources/budget_data.csv"
total_months = 0
net_total = 0
row = []
previous_profit_loss = 0
revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",0]
with open(csvpath) as file:
    csv_reader = csv.reader(file,delimiter=",")
    for row in csv_reader:
        print(row)

#The total number of months included in the dataset
        
with open(csvpath) as file:
    csv_reader = csv.reader(file, delimiter=",")
    next(csv_reader)
    prev_profit_loss = 0
    rows = list(csv_reader)
#The net total amount of "Profit/Losses" over the entire period
for row in rows:
    total_months += 1
    net_total += int(row[1])
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    current_profit_loss = int(row[1])
    revenue_change = current_profit_loss - previous_profit_loss
    revenue_change_list.append(revenue_change)

    prev_profit_loss = current_profit_loss

average_change = sum(revenue_change_list) / len(revenue_change_list)
#The greatest increase in profits (date and amount) over the entire period
if revenue_change > greatest_increase[1]:
    greatest_increase[1] = revenue_change
    greatest_increase[0] = row[0]

#The greatest decrease in profits (date and amount) over the entire period
if revenue_change < greatest_decrease[1]:
    greatest_decrease[1] = revenue_change
    greatest_decrease[0] = row[0]

print(f'Total number of months: {total_months}')
print(f'Net total profit/losses: ${net_total}')
print(f'changes in Profit/Losses: {revenue_change_list}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatesr Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
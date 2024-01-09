import os
import csv

csvpath = "../Resources/budget_data.csv"
# Initialize Variables
total_months = 0
net_total = 0
row = []
revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",0]
previous_profit_loss = 0
# Open the CSV file and read date
with open(csvpath) as file:
    csv_reader = csv.reader(file,delimiter=",")
    next(csv_reader) #Skip the header row. 
    rows = list(csv_reader)

#Calculate total months and net total profit/losses
for row in rows:
    total_months += 1
    net_total += int(row[1])

    #calculate changes in profit/losses and store then in a list
    current_profit_loss = int(row[1])
    revenue_change = current_profit_loss - previous_profit_loss
    revenue_change_list.append(revenue_change)
    prev_profit_loss = current_profit_loss

    #find the greatest increase and decrease in profits
    if revenue_change > greatest_increase[1]:
        greatest_increase[1] = revenue_change
        greatest_increase[0] = row[0]
    if revenue_change < greatest_decrease[1]:
        greatest_decrease[1] = revenue_change
        greatest_decrease[0] = row[0]

average_change = sum(revenue_change_list) / len(revenue_change_list)
#Print the results
print(f'Total number of months: {total_months}')
print(f'Net total profit/losses: ${net_total}')
print(f'changes in Profit/Losses: {revenue_change_list}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')

#write the results to a text file
output_file_path = "C:\\Users\\artsy\\OneDrive\\Desktop\\python-challenge-repo\\python-challenge\\analysis\\analysis_text.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Finacial Analysis\n")
    output_file.write("-----------------\n")
    output_file.write(f'Total number of months: {total_months}\n')
    output_file.write(f'Net total profit/losses: ${net_total}\n')
    output_file.write(f'Changes in Profit/Losses: {revenue_change_list}\n')
    output_file.write(f'Average Change: ${average_change:.2f}\n')
    output_file.write(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
    output_file.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')

print("Results have been exported to analysis_text.txt")

import os
import csv

budget_data = os.path.join("budget_data.csv")

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        pass
    row_count = csvreader.line_num - 1    


print('Financial Analysis')
print('------------------')
print(f"Total Months: {row_count}")


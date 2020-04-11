import os
import csv
from statistics import mean

budget_data = os.path.join("budget_data.csv")

netPL = 0

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_head = next(csvreader)

    months = len(list(csvreader))
     

with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    num_before = next(csv_reader)
    total = int(num_before[1])
    for line in csv_reader:
        total = total + int(line[1])


with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    first_row = next(csv_reader)
    change_list = []
    current_row = 0
    diff_value = 0
    previous_numb = 0
    
    for line in csv_reader:
        current_row += 1
        if current_row == 1:
            previous_numb = int(line[1])
        else:
            diff_value = int(line[1]) - previous_numb
            previous_numb = int(line[1])
            change_list.append(diff_value)

with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    amountList = []
    monthList = []

    for line in csv_reader:
        number = int(line[1])
        amountList.append(number)
        date = str(line[0])
        monthList.append(date)

    maximum = max(amountList)
    zipped = zip(amountList,monthList)

    best_month = ""
    for i in zipped:
        if i[0]== maximum:
            best_month = i[1]

with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    amountList = []
    monthList = []

    for line in csv_reader:
        number = int(line[1])
        amountList.append(number)
        date = str(line[0])
        monthList.append(date)
        
    minimum = min(amountList)
    zipped = zip(amountList,monthList)

    worst_month = ""
    for x in zipped:
        if x[0]== minimum:
            worst_month = x[1]



print('---------------------------')
print('Financial Analysis')
print('---------------------------')
print(f"Total Months: {months}")
print("Net Variation: " + str("${:,.2f}".format(total)))
print("Average Variation: " + str("${:,.2f}".format(round(mean(change_list)))))
print("Greatest Increase: " + best_month + "  " + '${:,.2f}'.format(maximum))
print("Greatest Decrease: " + worst_month + "   " + '${:,.2f}'.format(minimum)) 
print('---------------------------')


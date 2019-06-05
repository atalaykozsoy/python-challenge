
import csv
import itertools

dates = []
revenue = []

with open('PyBank.csv', 'r') as data:
    csvreader = csv.reader(data)

    for row in itertools.islice(csvreader, 1, None):
        dates.append(row[0])
        revenue.append(row[1])

number_of_months = len(dates)

total_revenue = 0
i = 0
for i in range(number_of_months):
    total_revenue = total_revenue + int(revenue[i])

monthly_change = []
j = 0
k = 0
for j in range (0, number_of_months):
    if j == 0:
        monthly_change.append(0)
    else:
        monthly_change.append(int(revenue[j])-int(revenue[k]))
        k = k + 1

sum_monthly_change = 0
m = 0
for m in range(number_of_months):
    sum_monthly_change = sum_monthly_change + int(monthly_change[m])
average_monthly_change = int (sum_monthly_change)/int(number_of_months - 1)

max_revenue_change = max(monthly_change)
max_index = monthly_change.index(max_revenue_change)
max_date = dates[max_index]

min_revenue_change = min(monthly_change)
min_index = monthly_change.index(min_revenue_change)
min_date = dates[min_index]


print("  Financial Analysis  ")
print("----------------------")
print("Total Months: " + str(number_of_months))
print("Total: $" + str(total_revenue))
print("Average Revenue Change: $" + str(average_monthly_change))
print("Greatest Increase in Revenue: " + str(max_date) + " $" + str(max_revenue_change))
print("Greatest Decrease in Revenue: " + str(min_date) + " $" + str(min_revenue_change))


txtpath = ("financial_analysis.txt")
with open(txtpath, "w") as txtfile:
    txtfile.write("  Financial Analysis  \n")
    txtfile.write("----------------------\n")
    txtfile.write("Total Months: " + str(number_of_months) + "\n")
    txtfile.write("Total: " + str(total_revenue) + "\n")
    txtfile.write("Average Revenue Change: " + str(average_monthly_change) + "\n")
    txtfile.write("Greatest Increase in Revenue: " + str(max_date) + " " + str(max_revenue_change) + "\n") 
    txtfile.write("Greatest Decrease in Revenue: " + str(min_date) + " " + str(min_revenue_change) + "\n")  
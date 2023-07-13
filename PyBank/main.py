import os
import csv

count = 0
total = 0
change1 = 0
change2 = change1
changelist = []
tempmax = 0
tempmin = 0
tempmaxname = ""
tempminname = ""

csvpath = os.path.join("Resources" , "budget_data.csv")

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)         #skip header row

        for row in csvreader:
            count += 1
            row[1] = int(row[1])
            change1= row[1]
            total += row[1]
            if count != 1:      #skip the first month; there was no change
                changelist.append(change1-change2)
            change2 = row[1]

            for i in range(len(changelist)):
                if tempmax < changelist[i]:
                    tempmaxname = row[0]
                    tempmax = changelist[i]

                if tempmin > changelist[i]:   
                    tempminname = row[0]
                    tempmin = changelist[i]

txtpath = os.path.join("Analysis" , "bankanalysis.txt")

with open(txtpath, "w") as txtfile:
    txtfile.write(f"Financial Analysis \n---------------------------- \n")
    txtfile.write(f"Total Months: {count} \n")
    txtfile.write(f"Total: ${total} \n")
    txtfile.write(f"Average Change: ${round(sum(changelist)/len(changelist),2)} \n")
    txtfile.write(f"Greatest Increase in Profits: {tempmaxname} (${tempmax}) \n")
    txtfile.write(f"Greatest Decrease in Profits: {tempminname} (${tempmin}) \n")

print(f"Financial Analysis \n----------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${round(sum(changelist)/len(changelist),2)}")
print(f"Greatest Increase in Profits: {tempmaxname} (${tempmax})")
print(f"Greatest Decrease in Profits: {tempminname} (${tempmin})")

import os
import csv
csvpath = os.path.join("Resources" , "budget_data.csv")

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)         #skip header row
        count = 0
        total = 0
        change1 = 0
        change2 = change1

        changelist = []
        for row in csvreader:
            count += 1
            row[1] = int(row[1])
            change1= row[1]
            total += row[1]
            if count != 1:      #skip the first month; there was no change
                changelist.append(change1-change2)
            # for i in range(len(changelist) -1):
            #      if changelist[i+1] > changelist[i]:
            #          tempmax = row[0]
            change2 = row[1]
                    
        print(f"Financial Analysis \n ----------------------------")    
        print(f"Total Months: {count}")
        print(f"Total: ${total}")
        print(f"Average Change: ${round(sum(changelist)/len(changelist),2)}")
        print(f"Greatest Increase in Profits: $ {max(changelist)}")
        print(f"Greatest Decrease in Profits: $ {min(changelist)}")
        print(tempmax)
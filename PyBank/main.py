import os
import csv
csvpath = os.path.join("Resources" , "budget_data.csv")

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader) #skip header row
        count = 0
        total = 0
        change1 = 0
        change2 = 0
        delta = 0
        for row in csvreader:
            count += 1
            row[1] = int(row[1])
            totalchange = row[1]
            change1= totalchange
            total += totalchange
        for row in csvreader:
            change2 = row[1]
            delta = change2+change1
            print(f"{delta} \n")    
            
        print(count)
        print(total)
            
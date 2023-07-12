import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        count = 0
        for row in csvreader:
            count += 1
        print(count)
            
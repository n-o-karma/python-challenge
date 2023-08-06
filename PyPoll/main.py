import os
import csv

totalcount = 0
numvotes = {}
tmpname = ''
names = []
csvpath = os.path.join("Resources" , "election_data.csv")

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)         #skip header row
        
        for row in csvreader:

            totalcount += 1
            tmpname = row[2]

            if tmpname not in names:
                names.append(tmpname)
                numvotes[tmpname] = 1
            elif tmpname in names:
                numvotes[tmpname] += 1

numvotes

totalcount

names

percents = {}
for key in numvotes:
    percents[key] = round(numvotes[key]/totalcount * 100,3)

percents

winner = max(zip(numvotes.values(),numvotes.keys()))
winner = winner[1]

print('Election Results')
print('-------------------------')
for name in names:
    print(f'{name}: {percents[name]}% ({numvotes[name]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

txtpath = os.path.join("Analysis" , "pollanalysis.txt")

with open(txtpath, "w") as txtfile:
    txtfile.write('Election Results \n')
    txtfile.write('------------------------- \n')
    for name in names:
        txtfile.write(f'{name}: {percents[name]}% ({numvotes[name]}) \n')
    txtfile.write('------------------------- \n')
    txtfile.write(f'Winner: {winner} \n')
    txtfile.write('------------------------- \n')
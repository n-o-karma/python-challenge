{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "eb6ae4fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "2988c9b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "totalcount = 0\n",
    "numvotes = {}\n",
    "tmpname = ''\n",
    "names = []\n",
    "csvpath = os.path.join(\"Resources\" , \"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "3b7224a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(csvpath) as csvfile:\n",
    "        csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "        header = next(csvreader)         #skip header row\n",
    "        \n",
    "        for row in csvreader:\n",
    "\n",
    "            totalcount += 1\n",
    "            tmpname = row[2]\n",
    "\n",
    "            if tmpname not in names:\n",
    "                names.append(tmpname)\n",
    "                numvotes[tmpname] = 1\n",
    "            elif tmpname in names:\n",
    "                numvotes[tmpname] += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "fda5bbfb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Charles Casper Stockham': 85213,\n",
       " 'Diana DeGette': 272892,\n",
       " 'Raymon Anthony Doane': 11606}"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numvotes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "d484a113",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "369711"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "totalcount"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "6b9736ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "c3af4d1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "percents = {}\n",
    "for key in numvotes:\n",
    "    percents[key] = round(numvotes[key]/totalcount * 100,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "2065a53c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Charles Casper Stockham': 23.049,\n",
       " 'Diana DeGette': 73.812,\n",
       " 'Raymon Anthony Doane': 3.139}"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "percents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "1dbcf1f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "winner = max(zip(numvotes.values(),numvotes.keys()))\n",
    "winner = winner[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "669af6bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Charles Casper Stockham: 23.049% (85213)\n",
      "Diana DeGette: 73.812% (272892)\n",
      "Raymon Anthony Doane: 3.139% (11606)\n",
      "-------------------------\n",
      "Winner: Diana DeGette\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "print('Election Results')\n",
    "print('-------------------------')\n",
    "for name in names:\n",
    "    print(f'{name}: {percents[name]}% ({numvotes[name]})')\n",
    "print('-------------------------')\n",
    "print(f'Winner: {winner}')\n",
    "print('-------------------------')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "13a63e88",
   "metadata": {},
   "outputs": [],
   "source": [
    "txtpath = os.path.join(\"Analysis\" , \"pollanalysis.txt\")\n",
    "\n",
    "with open(txtpath, \"w\") as txtfile:\n",
    "    txtfile.write('Election Results \\n')\n",
    "    txtfile.write('------------------------- \\n')\n",
    "    for name in names:\n",
    "        txtfile.write(f'{name}: {percents[name]}% ({numvotes[name]}) \\n')\n",
    "    txtfile.write('------------------------- \\n')\n",
    "    txtfile.write(f'Winner: {winner} \\n')\n",
    "    txtfile.write('------------------------- \\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca4c7aea",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "553d0ea7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

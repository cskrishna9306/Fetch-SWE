import sys
import csv
import payer
from datetime import datetime

if __name__ == "__main__":

    payers = []
    with open(sys.argv[2], mode = 'r') as f:
        #csv_dict = csv.DictReader(f)
        
        for row in csv.DictReader(f):
            payers.append(payer.Payer(row["payer"], int(row["points"]), datetime.strptime(row["timestamp"], "%Y-%m-%dT%H:%M:%SZ")))

    payers.sort()

    expenditure = int(sys.argv[1])

    for payer in payers:
        if expenditure == 0:
            break
        if expenditure > payer.points:
            expenditure -= payer.points
            payer.points = 0
        else:
            payer.points -= expenditure
            expenditure = 0

    payers_dict = {}
    for payer in payers:
        if payer.name not in payers_dict.keys():
            payers_dict[payer.name] = 0
        payers_dict[payer.name] += payer.points

    print(payers_dict)





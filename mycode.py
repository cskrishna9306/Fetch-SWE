import sys
import csv
import transaction
from datetime import datetime

if __name__ == "__main__":

    transactions = []
    with open(sys.argv[2], mode = 'r') as f:
        for row in csv.DictReader(f):
            transactions.append(transaction.Transaction(row["payer"], int(row["points"]), datetime.strptime(row["timestamp"], "%Y-%m-%dT%H:%M:%SZ")))
    
    transactions.sort()

    expenditure = int(sys.argv[1])

    for transaction in transactions:
        if expenditure == 0:
            break
        if expenditure > transaction.points:
            expenditure -= transaction.points
            transaction.points = 0
        else:
            transaction.points -= expenditure
            expenditure = 0

    #if expenditure

    payers_dict = {}
    for transaction in transaction:
        if transaction.payer not in payers_dict.keys():
            payers_dict[transaction.payer] = 0
        payers_dict[transaction.payer] += transaction.points

    print(payers_dict)



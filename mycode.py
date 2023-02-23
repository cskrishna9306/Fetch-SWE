import json
import sys
import csv
from datetime import datetime


class Transaction:
    def __init__(self, payer, points, timestamp):
        self.payer = payer
        self.points = points
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp
    
    def __str__(self):
        return f"Payer {self.payer} has {self.points} points on {self.timestamp}"
    
    def __repr__(self):
        return str(self)


def main():

    try:
        if sys.argv[2][-4:] != ".csv":
            raise FileNotFoundError

        transactions = []
        with open(sys.argv[2], mode = 'r') as f:
            for row in csv.DictReader(f):
                transactions.append(Transaction(row["payer"], int(row["points"]), datetime.strptime(row["timestamp"], "%Y-%m-%dT%H:%M:%SZ")))
    
        transactions.sort()

        expenditure = int(sys.argv[1])
        
        if expenditure < 0:
            raise ValueError

        for transaction in transactions:
            if expenditure == 0:
                break
            if expenditure > transaction.points:
                expenditure -= transaction.points
                transaction.points = 0
            else:
                transaction.points -= expenditure
                expenditure = 0

        payers_dict = {}
        for transaction in transactions:
            if transaction.payer not in payers_dict.keys():
                payers_dict[transaction.payer] = 0
            payers_dict[transaction.payer] += transaction.points

        print(json.dumps(payers_dict, indent=4))

    except FileNotFoundError:
        print(f"FileNotFoundError: {sys.argv[2]} is not a valid file name. Please ensure that the entered file exists as a CSV file in the same directory as {sys.argv[0]}.")
        print("Usage: {python|python3} mycode.py [POINTS] [FILE_NAME]")
    except ValueError:
        print(f"ValueError: {sys.argv[1]} is not a valid argument. Please enter positive integer values.")
        print("Usage: {python|python3} mycode.py [POINTS] [FILE_NAME]")


if __name__ == "__main__":
    main()

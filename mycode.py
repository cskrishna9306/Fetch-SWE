import json
import sys
import csv
from datetime import datetime

class Transaction:
    """This class holds information pertaining to each Transaction"""

    def __init__(self, payer, points, timestamp):
        self.payer = payer
        self.points = points
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp
    
    def __str__(self):
        return f"Transaction with {self.payer} has {self.points} points on {self.timestamp}"
    
    def __repr__(self):
        return str(self)


def main():

    try:
        # Check to see if the input file is a CSV file
        if sys.argv[2][-4:] != ".csv":
            raise FileNotFoundError

        # Parses and stores each transaction in the CSV file within a list
        transactions = []
        with open(sys.argv[2], mode = 'r') as f:
            for row in csv.DictReader(f):
                transactions.append(Transaction(row["payer"], int(row["points"]), datetime.strptime(row["timestamp"], "%Y-%m-%dT%H:%M:%SZ")))
    
        # Sorts the transactions by their respective timestamp
        transactions.sort()

        spending_points = int(sys.argv[1])
        
        # Throws a Value Error if the input points is negative
        if spending_points < 0:
            raise ValueError

        # Spends the points by following a Greedy approach
        for transaction in transactions:
            if spending_points == 0:
                break
            if spending_points > transaction.points:
                spending_points -= transaction.points
                transaction.points = 0
            else:
                transaction.points -= spending_points
                spending_points = 0

        # Creates a dictionary of all the payers and their respective points
        payers_dict = {}
        for transaction in transactions:
            if transaction.payer not in payers_dict.keys():
                payers_dict[transaction.payer] = 0
            payers_dict[transaction.payer] += transaction.points

        # Outputs the dictionary of all the payers and their remaining points
        print(json.dumps(payers_dict, indent=4))

    except FileNotFoundError: # Generates a custom error message for inputting incorrect file name
        print(f"FileNotFoundError: {sys.argv[2]} is not a valid file name. Please ensure that the entered file exists as a CSV file in the same directory as {sys.argv[0]}.")
        print("Usage: {python|python3} mycode.py [POINTS] [FILE_NAME]")
    except ValueError: # Generates a custom error message for inputting incorrect points
        print(f"ValueError: {sys.argv[1]} is not a valid argument. Please enter positive integer values.")
        print("Usage: {python|python3} mycode.py [POINTS] [FILE_NAME]")


if __name__ == "__main__":
    main()

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

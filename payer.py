class Payer:
    def __init__(self, name, points, timestamp):
        self.name = name
        self.points = points
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp
    
    def __str__(self):
        return f"Payer {self.name} has {self.points} points on {self.timestamp}"
    
    def __repr__(self):
        return str(self)

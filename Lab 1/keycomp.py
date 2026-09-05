class KeyComparisons:
    def __init__(self):
        self.numofkeycomp = 0
    
    def morethanb(self, a, b) -> bool:
        self.numofkeycomp += 1
        return a > b

    def lessthanb(self, a, b) -> bool:
        self.numofkeycomp += 1
        return a < b
    
    def equaltob(self, a, b) -> bool:
        self.numofkeycomp += 1
        return a == b
    
    def increasenum(self, incrementval):
        self.numofkeycomp += incrementval

    def decreasenum(self, decreaseval):
        self.numofkeycomp -= decreaseval
    
    def resetnum(self):
        self.numofkeycomp = 0
    
    def returnkeycomp(self):
        return self.numofkeycomp

    
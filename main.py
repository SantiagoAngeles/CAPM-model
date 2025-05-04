class Capm():
    def __init__(self, rf, beta, mr):
        self.rf = rf
        self.beta = beta
        self.mr = mr
    
    # rate = Capm(input())

    def capital_cost(self):
        cost = self.rf + self.beta *(self.mr - self.rf)
        return f"Cost of captial under CAPM model is {cost}"
class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest

    def value_after(self, n):
        return self.principal * (1 + self.interest)**n

    def __str__(self):
        return 'Principal - ${}, Interest rate - {}%'.format(self.principal, self.interest)


c = Investment(1000, 2.15)
print(c)

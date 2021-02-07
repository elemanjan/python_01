class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self):
        if self.amount > 10 and self.amount < 100:
            self.price = (self.amount * self.price)*0.1
        elif self.amount > 100:
            self.price = (self.amount * self.price)*0.2
        else:
            self.price = self.price * self.amount
        return self.price

    def make_purchase(self, x):
        if self.amount > x:
            self.amount -= x
        else:
            print('There are just {} items.'.format(self.amount))


z = Product('laptop', 50, 500)

print(z.get_price())
print(z.make_purchase(55))

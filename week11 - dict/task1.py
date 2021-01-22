item = {}
for i in range(5):
    product = input('enter product name: ')
    price = input('enter product price: ')
    item[product] = price

prod = input('enter product name to print price : ')
print(item[prod])
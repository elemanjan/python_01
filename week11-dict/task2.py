item = {}
for i in range(3):
    product = input('enter product name: ')
    price = int(input('enter product price in som: '))
    item[product] = price


price2 = int(input('enter price: '))

for itm in item:
    if item[itm] > price2:
        print(itm)
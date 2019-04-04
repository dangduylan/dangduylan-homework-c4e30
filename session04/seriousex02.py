prices = {
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3
}
stock = {
    'banana':6,
    'apple':0,
    'orange':32,
    'pear':15
}
myallfood = []
total = 0
for p in prices:
    for s in stock:
        if p == s:
            total = total + prices[p]*stock[s]
            myfood = {}
            myfood['name:'] = p
            myfood['prices:'] = prices[p]
            myfood['stock:'] = stock[s]
            myallfood.append(myfood)
for i in myallfood:
    for k in i:
        print(k,i[k])
    print()
print('If you sold all of your food, you would get:', total)



# yourmoney = int(input('Ban can gui so tien la(VND):'))
# ny = 0
# while True:
#     interest = 0.065 * yourmoney
#     yourmoney = yourmoney + interest
#     ny += 1
#     if ny == 9:
#         print('Your money after 9 years is:',yourmoney)
#         break

yourmoney = int(input('Ban can gui so tien la(VND):'))
n = 0
while True:
    interest = 0.065 * yourmoney
    yourmoney = yourmoney + interest
    n += 1
    if yourmoney // 1200000000 >=1:
        print('It takes',n, 'years to buy a 1.2 billion house')
        break
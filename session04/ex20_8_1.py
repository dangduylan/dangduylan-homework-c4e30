sentence = str(input("Enter your sentence:"))
sentence = sentence.lower()
Pool = {}
for i in sentence:
    if i not in Pool:
        Pool.setdefault(i,1)
    else:
        Pool[i] = Pool[i] + 1
for k,v in sorted(Pool.items()):
    if k != ' ':
        print(k,v)


     


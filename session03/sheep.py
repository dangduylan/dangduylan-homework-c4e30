sheepsize = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Lan and these are my sheep size')
print(sheepsize)
print("Now my biggest sheep has size", max(sheepsize), "let's shear it")
for i in range(len(sheepsize)):
    if sheepsize[i] == max(sheepsize):
        mp = i
sheepsize[mp] = 8
print('After shearing, here is my flock')
print(sheepsize)
month = int(input('The grow up process of your flock after (months):'))
n = 1
while True:
    if n < month+1:
        for i in range(month):
            print('MONTH', n,':')
            print('One month has passed, now here is my flock')
            for i in range(len(sheepsize)):
                sheepsize[i] += 50
            print(sheepsize)
            n += 1
            print("Now my biggest sheep has size", max(sheepsize), "let's shear it")
            for i in range(len(sheepsize)):
                if sheepsize[i] == max(sheepsize):
                    mp = i
            sheepsize[mp] = 8
            print('After shearing, here is my flock')
            print(sheepsize)
    else:
        break
sum = 0
for i in sheepsize:
    sum += i
print('My flock has size in total:', sum)
money = sum*2
print('I would get', sum,'* 2$ =', money,'$')
    



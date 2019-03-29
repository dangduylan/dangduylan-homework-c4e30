h = float(input('Enter Your height:'))
hm = h/100
w = float(input('Enter Your weight:'))
BMI = w/(hm*hm)
if BMI < 16:
    print('You are severely underweight')
elif 16 <= BMI < 18.5:
    print('You are underweight')
elif 18.5 <= BMI < 25:
    print('You are normal')
elif 25 <= BMI < 30:
    print('You are overweight')
else:
    print('You are obese')
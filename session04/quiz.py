# #quizex3:

# question = 'If x = 8, then what is the value of 4(x+3) ?'
# answer = {
#     1:35,
#     2:36,
#     3:40,
#     4:44
# }
# while True:
#     print(question)
#     for k in answer:
#         print(k,end = '. ')
#         print(answer[k])
#     your_choice = int(input('Your choice: '))
#     if your_choice == 4:
#         print('Bingo')
#         break
#     else:
#         print('You wrong, Try again!')
#         print() 

#quizex4:
quiz = [
    {
     'start': 'Answer the following algebra question:',
     'q': 'If x = 8, then what is the value of 4(x+3) ?',
     'a': '1. 35 \n2. 36 \n3. 40 \n4. 44',
     'true_answer': 4
    },
    {
     'start': 'Estimate this answer (exact calculation not needed):',
     'q': 'Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean',
     'a': '1. About 55 \nAbout 65 \nAbout 75 \nAbout 85',
     'true_answer': 2
     }
]
correct = 0
for i in quiz:
    print(i['start'])
    print(i['q'])
    print(i['a'])
    your_choice = int(input('Your choice: '))
    if your_choice == i['true_answer']:
        correct += 1
        print('Bingo')
    else:
        print('You wrong :(')
        print()
print('You correctly answer',correct,'out of 2 questions')
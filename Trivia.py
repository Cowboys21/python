print('Hello, welcome to trivia')
print('awnser all quastions in Yes or no')

ans = input('Are you ready to play yes/no? ')
score = 0
total_q = 4
if ans.lower() == 'yes' :
    
    ans = input('1. Is Aarshabh stupid? ')
if ans.lower() == 'yes':
        score += 1
        print('you are correct!!')
else:
        print('you are very wrong')

ans = input('2. Are papa and mama smart, cute ,and amazing ? ')
if ans.lower() == 'yes':
        score += 1
        print('you are correct!!')
else:
        print('you are very wrong')

ans = input('3. Does your sneeze travel 80 mph or any number less? ')
if ans.lower() == 'no':
        score += 1
        print('you are correct!!')
else:
        print('You are wrong it traves 100 mph')
        
print('For this last question you will have to type a number.')

ans = input('4. How many hours does it take to digest you food ? ')
if ans.lower() == '12':
        score += 1
        print('wow, you are smart!!')
else:
        print('Wrong! It takes 12 hours')
print('thank you for playing, you got',score,"questions correct")        

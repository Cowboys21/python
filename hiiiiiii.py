print('What is your name?')
myName = input()
myName = myName.upper()
have_high_income = True
has_good_credit = True
print('It is good to meet you, ' + myName)
print("I'm going to ask some questions to approve of your loan, " + myName)
print('First of all...')
X = input('Do you have high income, type Yes or No ')

print("Value Entered by user, " + X)
X = X.lower().strip()

if X == 'no':
    have_high_income = False

else :
    have_high_income = True

if have_high_income == True:
    print('Congratulations your loan is approved')
else :
    print('Sorry you loser no loan')



# main change between list and tuple is that list is changable tuple isn't



# creating list
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']



# Accessing one item
dog = dogs[0]
print(dog.title())
# the index of an item is always one less than its position in the list.
dogo = dogs[-1]
print(dogo)
# use "-" to use last things on list



# Access all elements in list
for dog in dogs:
    print(dog)




#loop notes
#"for" tells Python to get ready to use a loop.




# adding things inside loop
for dog in dogs:
    print('I poop on and love' + dog + 's.')



#inside/outside loop
for dog in dogs:
    print('I like ' + dog + 's.')
    print('No, I really really like ' + dog +'s!\n')
    
print("\nThat's just how I feel about dogs.")




#enumerating lists
#enumerate()function tracks the index of each item
#for you, as it loops through the list
print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index + 1)
    print("Place: " + place + " Dog: " + dog.title())




#loop practice
sports =['football','basketball','soccer']
for sport in sports:
    print('I like '+ sport) 




#modify element in list
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs[0] = 'australian shepherd'
print(dogs)



#finding element in a list
print(dogs.index('australian cattle dog'))




#Testing if item is in list
# you can test using the "in" function
print('australian cattle dog' in dogs)
print('poodle' in dogs)



# adding/appending things to list
#append means add on the end of line
dogs.append(' german shepard')
for dog in dogs:
    print(dog.title() + "s are cool.")



    
#inserting items
#inserting means you can  add put anywhere in list
dogs.insert(1, 'mutt')
print(dogs)




#create empty list
usernames =[]
#how to add items
usernames.append('turd')
usernames.append('poop')
usernames.append('toilet')
#how to use list
for username in usernames:
    print("We need, " + username.title() + '!')
#use user in sentence
print("\nThank you for being our very first user, " + usernames[0].title() + '!')
print("And a warm welcome to our newest user, " + usernames[-1].title() + '!')




#sorting list
#put in alphabetic order
usernames.sort()
#display in order
print("Our students are poops are in alphabetical order.")
for username in usernames:
    print(username.title())
#reverse alphabetical order
usernames.sort(reverse=True)
print("our tutties will now be in reverse")
for username in usernames:
    print(username.title())




#Numerical list
numbers = [2,4,3,1]
#sort numbers
numbers.sort()
print(numbers)
# reverse number list
numbers.sort(reverse=True)
print(numbers)




#Finding length of list
user_count = len(usernames)
print(user_count)
print("We have " + str(user_count) + " users!")
usernames.append('fart')
user_count = len(usernames)
print("We have " + str(user_count) + " users!")
print("This is how you put the count in a string: " + str(user_count))



#removing items from list

#removing item by position from list
del dogs[0]
print(dogs)

#removing by value
dogs.remove('mutt')
print(dogs)




#popping  items from list
#It removes the last item from the list,
#and gives it to us so we can work with it
last_dog = dogs.pop()
print(last_dog)
print(dogs)
#how to pop from anywhere in list
first_dog = dogs.pop(0)
print(first_dog)
print(dogs)




# slicing list
first_batch = usernames[0:3]
for XYZ in first_batch:
    print(XYZ.title())
# slicing part of a list
first_batch = usernames[1:3]
for user in first_batch:
    print(user.title())




#copying list
copy_poop = usernames[:]
print("The full copied list:\n\t", copy_poop)
#changing copied list
del copy_poop[0]
del copy_poop[0]
print("\nTwo users removed from copied list:\n\t", copy_poop)
#original list
print("\nThe original list:\n\t", usernames)



#number functions
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

#range function
# The range() function helps us generate long lists of numbers.
for number in range(1,11):
    print(number)
#print first ten odd numbers
for number in range(1,21,2):
    print (number)



#list function
#list function takes in a range, and turns it into a list
numbers = list(range(1,11))
print(numbers)
numbers = list(range(1,1000001))
print("The list 'numbers' has " + str(len(numbers)) + " numbers in it.")
# "str(len(numbers))" takes length of list and turns it into string that can be printed
print("\nThe last ten numbers in the list are:")
for number in numbers[-10:]:
    print(number)
# numbers[-10:]gives us a slice of the listnumbers[-10:]
# gives us everything from that item to the end of the list.




#min max and sum
ages = [13, 9, 42, 37]
youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)
print("The youngest person is" + str(youngest) + "years old.")
print("Our most handsom is " + str(oldest) + " years old.")
print("together we are " + str(total_years) + "years old.")




#Numerical comprehensions
squares = []
for number in range(1,33):
    new_square = number**2
    squares.append(new_square)
for square in squares:
    print(square)

#Exercises
#multiple of ten
multiples = []
for number in range (1,11):
    multiples.append(number*10)
for multiple in multiples:
    print(multiple)
    
#Non-numberical comprehension
great_usernames = []
for username in usernames:
    great_usernames.append(username.title() + " the great!")
for great_username in great_usernames:
    print("Hello," + great_username)




#strings as list of characters
message = "Hello!"
for letter in message:
    print(letter)
#create list from string
message = "Hello world!"
message_list = list(message)
print(message_list)




#slicing string
#slicing characters
message = "Hello World!"
first_char = message[0]
last_char = message[-1]
print(first_char, last_char)
#taking slices
message = "Hello World!"
first_three = message[:3]
last_three = message[-3:]
print(first_three, last_three)




#Finding substrings
#A substring is a series of characters that appears in a string.
message = "Aarshabh likes to catch these hands"
hands = 'hands' in message
print(hands)
# The find() method tells you the index at which the substring begins.
hands_index = message.find('hand')
print(hands_index)
#If the substring appears more than once, you will miss the other substrings.

#If you want to find the last appearance of a substring,
#you can use the rfind() function:
message = "I like to punch Aarshabh and punch him until he's bleeding"
hands = message.rfind('punch')
print(hands)




#replacing substrings
message = "I like to punch Aarshabh and punch him until he's bleeding"
messages = message.replace('bleeding','dead')
print(messages)




#counting substring
#how many times a substring appears within a string, you can use the count() method.
poop = "poop poop poop poop poop poop poop poop poop poop poop poop poop poop"
number_poop = poop.count('poop')
print(number_poop)




#splitting strings
words = message.split(' ')
print(words)




#exercise
for messa in message:
    
    print(messa)




#Tuples notes

#Tuples are basically lists that can never be changed
    
#you use parentheses instead of square brackets
    
#Once you have a tuple, you can access individual elements just
#like you can with a list, and you can loop through the tuple with a for loop.




#Tuples in string
colors = ('red', 'green', 'blue')
print("The first color is: " + colors[0])




#Using tuples to make string
poop = 'Aarshabh'
print("My baby brother is named " + poop +".")




#%s" and "%d". These are placeholders.
#%s is for string
#%d is for number

#When Python sees the "%s" placeholder, it looks
#ahead and pulls in the first argument after the % sign:
print("My brother is named %s." % poop)
best_family = ('mama', 'papa', 'Aarshabh')
print("I love my %s, my %s, and %s." %(best_family[0], best_family[1], best_family[2]))




#String formatting with numbers
#how to add number in string
number = 21
print("My favorite number is " + str(number)+".")
print("My favorite number is %d." % number)
#The format string "%d" takes care of this for us.
#If you want to use a series of numbers,
#you pack them into a tuple just like we saw with strings:
numbers = [7, 23, 42]
print("My favorite numbers are %d, %d, and %d." % (numbers[0], numbers[1], numbers[2]))
#You can mix string and numerical placeholders in any order you want.
names = ['eric', 'ever']
numbers = [23, 2]
print("%s's favorite number is %d, and %s's favorite number is %d." % (names[0].title(), numbers[0], names[1].title(), numbers[1]))

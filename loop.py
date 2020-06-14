# 1 - You can have a list with a million items in it, and in three lines of code you can write a
# sentence for each of those million items.


# 2 - We use a loop to access all the elements in a list. A loop is a block of
# that repeats itself until it runs out of items to work with, or until
# a certain condition is met.

# 3 - The keyword "for" tells Python to get ready to use a loop.

leaders = ['Donald Trump', 'Kim Jong', 'Putin']

for leader in leaders:
    print(leader)
    print(leader + ' is a leader')
    print("these people lead countries " + leader + ' s!\n')

print (leaders)

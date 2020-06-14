import pickle
#import os
#os.system("clr")


what_height = input('What is your height in feet?(round to the nearest foot): ')
print(type(what_height))
inches = 12 * int(what_height)

pickle.dump(inches, open("inches.dat","wb"))

#inches = pickle.dump(inches, open("height.dat","rb"))

names = pickle.load(open("inches.dat","rb"))

print("Original list " + str(names))

#height.add("5 feet")

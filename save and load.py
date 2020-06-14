import pickle
import os
os.system("clr")

# Create list
names = ["Angus Young", "Malcolm Young", "Bon Scott"]

# Print the list
print("Original list")
print(names)

# Save the list
pickle.dump(names, open("names.dat","wb"))

# Change
names.remove("Bon Scott")
pickle.dump(names, open("names.dat","wb"))

# Print the list
print("Changed List")
print(names)

# Load the saved data
names = pickle.load(open("names.dat","rb"))

# Print the list
print("Original list")
print(names)
#x =  os.path.abspath("names.dat")
#print(x)

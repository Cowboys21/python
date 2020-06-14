from datetime import datetime

print("you use it to execute a block of code multiple times")
i = 1
while i <= 5 :
    print("*" * i) 
    i = i + 11
print("done")




now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", now)

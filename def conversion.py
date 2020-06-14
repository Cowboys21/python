def minutes_to_hours(seconds, minutes=70 ):
    hours = minutes / 60 + seconds / 3600
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

print(minutes_to_hours(70, 300))
print(seconds_to_hours(7200))

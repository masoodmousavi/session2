seconds = int(input("pls enter your seconds: "))

hour = seconds
minutse = seconds


minutse = minutse % 3600
hour = hour / 3600            
hour = int(hour)


minutse_to_seconds = minutse
sec = minutse_to_seconds


minutse_to_seconds = minutse / 60
sec = sec % 60


minutse = int(minutse)
minutse_to_seconds = int(minutse_to_seconds)
sec = int(sec)


print("hour",hour)
print("minuts",minutse_to_seconds)
print("seconds",sec)

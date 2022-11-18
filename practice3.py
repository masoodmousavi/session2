
counter = 0
sum = 0

while True:

    number = input("enter number or type exit: ")
    if number == "exit":
        break
    else:
        sum += float(number)
        counter = counter +1


average = sum/counter
print("student score average:",average)

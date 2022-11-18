fib = int(input("pls enter your fibo number: "))


a = 1
b = 0

for i in range(fib):

    result = a + b
    a = b
    b = result
    print(result)    

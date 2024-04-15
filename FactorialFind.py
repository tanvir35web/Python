user_input = int(input("Enter a number to find its Factorial: "))

factorial = 1;
for i in range (1, (user_input + 1)):
    factorial = factorial * i
print(factorial)
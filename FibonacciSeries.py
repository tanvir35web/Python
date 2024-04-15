# Print a Fibonacci series of upto 10

a = 1
b = 2
print("\n" "The Fibonacci Series is : ")
for i in range(10):
    print(a, end=" ")
    sum = a + b
    a = b
    b = sum
print("\n")
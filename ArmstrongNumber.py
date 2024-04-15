#Check Armstrong Number

user_input = input("Enter a Number to it Armstrong Number or Not : ")
number_length = len(user_input)

sum = 0
for i in user_input:
    sum = sum + int(i)**number_length

if int(user_input) == sum:
    print(user_input, "is an Armstrong Number")
else:
    print(user_input, "is not an Armstrong Number")
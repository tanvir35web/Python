#Largest value finder from three


number_one = int(input("Enter 1st number: ")) 
number_two = int(input("Enter 2nd number: ")) 
number_three = int(input("Enter 3rd number: ")) 

if number_one > number_two and number_one > number_three:
    print(number_one, "is the largest number")
elif number_two > number_three and number_two > number_one:
    print(number_two, "is the largest number")
else:
    print(number_three, "is the largest number")
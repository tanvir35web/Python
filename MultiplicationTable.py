# Multiplication table list print 

user_input = input("Enter a number to see its multiplication list: ")
user_input_typeCast = int(user_input) # convert string to integer number using type cast method

for i in range(1, 11):
     print( user_input_typeCast, "x", i, "=", i * user_input_typeCast)
  
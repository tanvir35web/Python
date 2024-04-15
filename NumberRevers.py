user_input = int(input("Enter a number to revers it: "))

temp = 0
for i in str(user_input):
    last_digit = user_input % 10
    temp = temp*10 + last_digit
    user_input = user_input // 10


print(temp)

# user_input = int(input("Enter a number to reverse it: "))

# temp = 0
# for _ in str(user_input):
#     last_digit = user_input % 10
#     temp = (temp * 10) + last_digit
#     user_input = user_input // 10

# print(temp)

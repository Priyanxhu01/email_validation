import re
# \w = search the charater, ? = print the boolean expression (0,1)
# search the value in back side to use "$"
# r'\ and \\ escape it properly.
email_condition="^[a-z]+[r'\'._]?[a-z 0-9]+[@]\\w+[.]\\w{2,3}$"
user_email = input("Enter your email: ")

if re.search(email_condition,user_email):
    print("Right email.!")

else:
    print("Wrong email.!")
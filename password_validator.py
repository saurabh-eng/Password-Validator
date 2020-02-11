import re

while True:
    try:
        PASSWORD = str(input("Please Enter a password:"))
        if len(PASSWORD) == 0:
            raise ValueError
    except ValueError:
        print("Input entered is blank,Please enter a password between 8 to 16 characters")
        continue
    else:
        break
if len(PASSWORD) > 0:
    PASSWORD_PATTERN = re.compile(r'((?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&*+-/])(?=.*[A-Z])(?!.* ).{8,16})')
    if re.match(PASSWORD_PATTERN, PASSWORD):
        print("Valid Password")
    else:
        print("Invalid Password")
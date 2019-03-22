"""Mitchell Marks"""

while True:
    try:
        MIN_PASSWORD_LENGTH = int(input("Specify a minimum password length: "))
        break
    except ValueError or NameError:
        print("Enter a valid length, you simpleton")
while True:
    try:
        password = input("Please enter a valid password {} characters long)".format(MIN_PASSWORD_LENGTH))
        password_length = len(password)
    except ValueError:
        print("You managed to screw this up? -_-")
    if password_length < MIN_PASSWORD_LENGTH:
        print("You managed to screw this up? -_-")
    else:
        break
print("*" * password_length)
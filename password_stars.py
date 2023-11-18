MINIMUM_PASSWORD_LENGTH = 10
password = input("Enter password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Invalid password, should be at least 10 characters")
    password = input("Enter password: ")
print("Password: ", "*"*len(password))

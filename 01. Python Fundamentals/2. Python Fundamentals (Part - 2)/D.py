# 4. Nesting

username = input("Username: ")
password = input("Password: ")

if username == "adom" and password == "Adom123@$":
    print("Login Successfull")
else:
    if username != "adom":
        print("Wrong Username")
    elif password != "Adom123@$":
        print("Wrong Password")
    else:
        print("Something went wrong. Please try again...")
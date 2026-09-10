username = "student"
password = "1234"

u = input("Username: ")
p = input("Password: ")

if u == username and p == password:
    print("Login successful!")
    print("Welcome to LMS")
else:
    print("Invalid login")

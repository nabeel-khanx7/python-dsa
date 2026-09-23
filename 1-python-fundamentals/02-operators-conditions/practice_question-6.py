# Practice Question 6 - Login System
# Check username and password.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login successful.")
else:
    print("Invalid username or password.")
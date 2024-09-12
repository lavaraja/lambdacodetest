import re

class UserValidator:
    def __init__(self):
        self.users = {
            "john_doe": "password123",
            "jane_smith": "securePass456"
        }
    
    def validate_login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False
    
    def validate_username(self, username):
        if not username:
            return False
        if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
            return False
        return True
    
    def validate_password(self, password):
        if len(password) < 8:
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        return True

# Example usage
validator = UserValidator()

# Test login
username = input("Enter username: ")
password = input("Enter password: ")

if validator.validate_username(username) and validator.validate_password(password):
    if validator.validate_login(username, password):
        print("Login successful!")
    else:
        print("Invalid credentials.")
else:
    print("Invalid username or password format.")

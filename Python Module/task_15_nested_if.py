'''
#Name: Prasanna Sai
#objective: Use nested conditions with a function + basic validation + formatted output.
#task: Validate username and password using nested if statements.
'''

def authenticate_user(username, password):
    """
    Checks username and password using nested if blocks, with validation for blank inputs.
    """
    # Validation for blank/empty inputs
    if not username or not username.strip():
        return "Authentication Error: Username cannot be blank."
    if not password or not password.strip():
        return "Authentication Error: Password cannot be blank."
        
    # Expected correct credentials
    db_username = "admin"
    db_password = "pass123"
    
    # Nested If statements
    if username == db_username:
        if password == db_password:
            return "Access Granted: Welcome, administrator!"
        else:
            return "Access Denied: Incorrect password."
    else:
        return "Access Denied: Username not found."

if __name__ == "__main__":
    # Test cases
    test_user = "admin"
    test_pwd = "pass123"
    
    print("Testing credentials validation:")
    print(f"Username: '{test_user}', Password: '{test_pwd}'")
    status = authenticate_user(test_user, test_pwd)
    print(f"Result: {status}\n")
    
    print("Testing invalid username:")
    print("Username: 'user1', Password: 'pass123'")
    status_wrong_user = authenticate_user("user1", test_pwd)
    print(f"Result: {status_wrong_user}\n")
    
    print("Testing invalid password:")
    print("Username: 'admin', Password: 'wrongpassword'")
    status_wrong_pwd = authenticate_user(test_user, "wrongpassword")
    print(f"Result: {status_wrong_pwd}\n")
    
    print("Testing blank input:")
    status_blank = authenticate_user("", "pass")
    print(f"Result: {status_blank}")

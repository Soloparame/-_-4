import hashlib

# A basic function to hash passwords for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register():
    print("Register an account")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Hash the password for security
    hashed_password = hash_password(password)
    
    # Save user credentials to a file (for simplicity, we're using a file to store data)
    with open("users.txt", "a") as file:
        file.write(f"{username},{hashed_password}\n")
    
    print("Registration successful!")

# Function to log in
def login():
    print("\nLogin to your account")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    hashed_password = hash_password(password)
    
    # Check if the user exists in the file
    with open("users.txt", "r") as file:
        users = file.readlines()
    
    for user in users:
        saved_username, saved_password = user.strip().split(",")
        if username == saved_username and hashed_password == saved_password:
            print(f"\nWelcome, {username}! Accessing secured page...")
            secured_page()
            return True
    
    print("Invalid username or password.")
    return False

# A secured page that can only be accessed after login
def secured_page():
    print("\n--- Secured Page ---")
    print("You have successfully accessed a protected area of the system.")

# Main menu
def main():
    while True:
        print("\n--- Authentication System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

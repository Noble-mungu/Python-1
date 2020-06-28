import user
 
def create_user(fname,lname,password):
    """
    Create a new user account

    """
    new_user = user(fname,lname,password)
    return new_user

def save_user(user):
    """
    Function to save user 
    """
    user.save_user()

def verify_user():
    """
    Function to verify user
    """
    user.verify_user(user)

def new_password():
    """
    Function to generte new password
    """
    new_password = password()
    return new_password

def con_password():
    """
    Function to confirm password
    """
    con_password = confirm_password()
    return con_password
  
def main():
    print("Welcome to password locker.")
    user_name = input("Name:")

    print(f"Hello {user_name}.What would you like to do ?")

    print('\n')

    while True:
        print("Use these short codes:nw - create a new user, lg-login.")
        break





if __name__ == '__main__':
    main()








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
        print("Use these short codes navigate through the app:\n nw - create a new user \n lg-login  \n ex-exit .")

        short_code = input(" Enter your choice:").lower()

        if short_code == 'nw':


            print("New Account")
            print("-"*50)
            first_name = input("Enter your First name:")
            last_name = input("Enter your last name:")
            password = input("Enter your password:")
        
            save_user(create_user(first_name,last_name,password))('\n')
            print(f"New account{first_name} {last_name} created")

       # elif password == con_password :
        #    print("Password doesnt match")
        elif short_code =='lg' :
            print("-"*50)
            print(' ')
            print("To log in enter your user name and password")
            user_name = input("Enter user name:").strip()
            password = str(input("Enter password:"))
            user_exist == verify_user(user_name,password) 
        if user_exist == user_name:
            print(" ")
            print(f"Welcome {user_name}.Please choose an option")
            print(' ')  
                   



               
if __name__ == '__main__':
    main()






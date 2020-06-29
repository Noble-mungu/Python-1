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

        short_codes = input("Enter your choice:").lower().strip()
        if short_code == 'ex':
            break
        elif short_code == 'nw' :
            print("New Account")
            print("-"*50)
            first_name = input("Enter your First name:").strip()
            last_name = input("Enter your last name:").strip()
            password = input("Enter your password:").strip()
            con_password =input("Confirm password:").strip()

            save_user(create_user(first_name,last_name,password))
        elif password != con_password :
            print("Password doesnt match")
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
                while True:
                    print("-"*50)
                    print('Navigation codes:\n cc-Create a credential \n dc-Display Credential')
                    if short_code =='ex':
                        print(" ")
                        print(f"Thank you {user_name} for using this app")
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print("Enter your details")
                        site_name = input('Enter the site\'s name:').strip()
                        account_name = input('Enter your account name:').strip()
                        while True:
                            print(' ')
                            print("-"*50)
                            print('Choose an optionfor entering a password:\n ep-enter existing pasword \n gn-generate password \n ex-exit ')
                            short_code = input("Enter your choice").lower().strip()
                            print("-"*50)
                            if psw_choice == 'ep':
                                    print(' ')
                                    password =input("Enter your password:").strip
                                    break
                            elif psw_choice == 'gn':
                                    password = generate_password()
                                    break
                            elif psw_choice == 'ex':
                                    break
                            else:
                                    print("Exiting.Try again")
                        save_credential(create_credential(user_name,site_name,account_name,password))
                        print(' ')
                        print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
                        print(' ')
                    elif short_code == 'dc':
                        print(' ')
                        if display_credentials(user_name):
                            print('Your credentials')
                            print(' ')
                            for credential in display_credentials(user_name):
                                print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print(' ')  
                        else:
                            print(' ')
                            print("No credentials saved yet")
                            print(' ')
                    elif short_code == 'copy':
                        print(' ')
                        chosen_site = input('Enter the site name  to copy: ')
                        copy_credential(chosen_site)
                        print('')
                    else:
                        print('Oops! Wrong option entered. Try again.')

            else: 
                print(' ')
                print('Oops! Wrong details entered. Try again or Create an Account.')       
        
        else:
            print("-"*50)
            print(' ')
            print('Oops! Wrong option entered. Try again.')
                
               
if __name__ == '__main__':
     main()
     






#!/urs/bin/env python3.6
from user import User
from credential import Credential


def create_user(user_name,user_login):
    '''
    Function to create new user
    '''
    new_user = User(user_name,user_login)
    return new_user

def save_user(user):
    '''
    Function to saver new user
    '''
    user.save_user()

def create_credential(credential_name,user_name,password):
    '''
    Function that creates new credentials for a given user account
    '''
    new_credential =Credential(account_name,account_userName,password)
    return new_credential

def delete_credential(credential):
    '''
    function to delete user
    '''
    credential.delete_user()

def save_credential(credential):
    """
    Function to save Credentials to the credentials list
    """
    credential.save_credential()

def display_credentials():
    """
    Function that returns all the saved credential.
    """
    return Credential.display_credential()

def find_credential(name):
    '''
    function for finding credential
    '''
    
    return Credential.find_by_name(name) 

def main():
    print("Hello Welcome to your Accounts Password Store...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code =='CA':
        print("Sign Up")
        print('*' * 50)
        username = input("User_Name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_user(user_name, user_login))
        print(f"A new Account for {user_name} has been created")
        print(f"You can now login to your {user_name} account using your password.")
        print ('\n')

    while True




if __name__ == '__main__':
    main()

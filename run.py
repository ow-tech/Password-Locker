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
    new_credential =Credential(credential_name,user_name,password)
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

def display_credential():
    """
    Function that returns all the saved credential.
    """
    return Credential.display_credential()

def find_credential(name):
    '''
    function for finding credential
    '''
    
    return Credential.find_by_name(name) 

def generate_Password():
    '''
    generates a random password for credential
    '''
    generatedPassword= Credential.genarate_password()
    return generatedPassword

def main():
    print("Hello Welcome to your Pass Word Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to Pass Word Locker to create an account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n ex ->exit Pass Word Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create a Pass Word Locker Account")
            print("_"*100)
            account_name = input('user_name:')
            print ('\n')
            pwd = input('user_login : ')
            print ('\n')
            save_user(create_user(user_name,pwd,)) 
            print ('\n')
            print(f"A New {user_name} Account with the user name  {user_name} has been created.")
            print(f"You can now login to your {account_name} account using your password.")
            print ('\n')
        elif short_code == 'ln':
                    print("Enter your User_name and your User_login to log in:")
                    username = input("user_name: ")
                    userlogin = input ("user_login: ")
                    # login_user(user_name,user_login)
                    if (username == "Alex123" and userlogin =="123alex"):
                        print(f"Hello {username}, Welcome back to Password Locker")
                        print('\n')
                    else:
                        print("Credentials do not match existing user")
                    

if __name__ == '__main__':
    main()                            

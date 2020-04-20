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
    function to delete credential
    '''
    credential.delete_credential()

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
                    while True:
                            print('''
                            Use these short codes:
                            CA -> Create new credential.
                            DC -> Display your credential list
                            DEL -> Delete credential
                            EX ->Log out your credential account.''')
                            short_code = input().upper()
                            if short_code == "CA":
                                print("Create new credential")
                                print('_' * 20)
                                credential_name = input('Credential name:')
                                print('\n')
                                user_name = input(f"{credential_name} user name:")
                                print('\n')
                                print('*' * 20)
                                pwd = input(f"{credential_name} password:")
                                save_credential(create_credential(credential_name,user_name,pwd))
                                print('\n')
                                print(f"A New {credential_name} Account with the user name  {user_name} has been created.")
                                print ('\n')
                            elif short_code == 'DC':
                                if display_credential():
                                        print("Here is your credential")
                                        print('\n')
                                        for credential in display_credential():
                                            print(f"Credential name:{credential.credential_name}  User name: {credential.user_name} Password:{credential.password}")
                                            print('\n')
                                else:
                                    print('\n')
                                    print("You don't seem to have created any account yet")
                                    print('\n')
                            elif short_code =="DEL":
                                print('\n')
                                print("Enter the account name you want to delete")
                                name = input().lower()
                                if find_credential(name):
                                    search_credential = find_credential(name)
                                    print("_"*50)
                                    search_credential.delete_credential()
                                    print('\n')
                                    print(f"Your stored credentials for : {search_credential.credential_name} successfully deleted!!!")
                                    print('\n')
                            elif short_code == "EX":
                                print('\n')
                                print(f"You have logged out your {account_name} account")
                                print('\n')
                                break  
                    else:
                        print("Credentials do not match existing user")           
        else:
            print('\n')
            print("WRONG PASSWORD!! PLEASE ENTER CORRECT PASSWORD TO LOGIN")
            print('\n')
            print('\n')

if __name__ == '__main__':
    main()                            

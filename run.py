#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(user_name,user_password):
    '''
    Function to create new user
    '''
    new_user = User(user_name, user_password)
    return new_user

def save_user(user):
    '''
    Function to saver new user
    '''
    user.save_user()

def create_credential(credential_name, user_name, account_password):
    '''
    Function that creates new credentials for a given user account
    '''
    new_credential = Credential(credential_name, user_name, account_password)
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
    return Credential.display_all_credentials()

def find_credential(name):
    '''
    function for finding credential
    '''
    
    return Credential.find_by_name(name) 
def find_by_name(name):
    return Credential.find_by_name(name)

def generate_password():
    '''
    generates a random password for credential
    '''
    generatedPassword = Credential.genarate_password()
    return generatedPassword

def main():
    # global userlogin 
    print("Hello Welcome to your Pass Word Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to Pass Word Locker to create an account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n SU -> SIGN UP.\n ex ->exit Pass Word Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create a Pass Word Locker Account")
            print("_"*100)
            account_name = input('user_name:')
            print ('\n')
            userlogin = input('user_login : ')
            print ('\n')
            save_user(create_user(user_name, userlogin)) 
            print ('\n')
            print(f"A New {user_name} Account with the user name  {user_name} has been created.")
            print(f"You can now Login")
            print ('\n')
            while True:
                def login():
                    print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n ex ->exit Pass Word Locker. ")
                    short_code = input().lower()
                    if short_code == 'ln':
                        print("Enter your User_login to log in: ")
                        # user_name = input("user_name: ").lower()
                        user_login = input ("user_login: ").lower()
                        if user_login == userlogin:
                            print("_"*100)
                            while True:
                                print(" Use these short codes:\n CA -> Create new credential.\n DC -> Display your credential\n DEL -> Delete credential\n EX ->Log out your credential account.")
                                short_code = input('Enter Short Code: ').lower()
                                
                                if short_code == "ca":
                                    print('@'*50)
                                    account_name = input('Acount Name/ Credential Account: ')
                                    print ('\n')
                                    account_user_name = input(f'{account_name} User Name: ')
                                    print ('\n')
                                    while True:
                                        print('Use these short codes:\n GE -> Let Pass Locker Generate a Password for you.\n HA -> Already Have a Password, Type it Mannualy')
                                        short_code = input('Enter Short Code: ').lower()
                                        if short_code == 'ha':
                                            account_password = input(f'{account_name}\'s Password: ')
                                            break
                                        elif short_code =='ge':
                                            account_password = generate_password()
                                            print(f'Your Generated Password is: {account_password}')
                                            print(account_password)
                                            break
                                    print ('\n')
                                    save_credential(create_credential(account_name, account_user_name, account_password))
                                    print('\n')
                                    print(f"A New {account_name} Account with the user name  {account_user_name} has been created.")
                                    print ('\n')
                                elif short_code == 'dc':
                                    try:
                                        print('HERE YOUR CREDENTIALS')
                                        print('\n')
                                        print('^'*50)
                                        for credential in display_credential():
                                            print('^'*50)
                                            print(f"Credential name:{credential.account_name}  User name: {credential.account_user_name} Password:{credential.account_password}")
                                            print('\n')
                                    except (IndexError, ValueError):
                                        print('^'*50)
                                        print('YOU HAVE NO CREDENTIALS YET')
                                elif short_code == 'del':
                                    print('\n')
                                    to_be_deleted = input('Enter Credential\'s or Account\'s Name to DELETE: ')
                                    credential_found = find_by_name(to_be_deleted)
                                    while True:
                                        delete_credential(credential_found)
                                        print(f'Credential {credential_found} DELETED')
                                        break
                                elif short_code =='ex':
                                    login()
                    else:
                        print("_"*50)
                        print(" ")
                        print("Credentials do not match existing user \n TRY AGAIN OR ANOTHER OPTION")
                        print("_"*50)
                        login()
                login()     
        elif short_code == 'ln':
            login()
        elif short_code == "ex":
            print(f"Thanks {user_name} for your time.I hope you enjoyed my service.Bye...")
            break
        else:
            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()


    
# #!/urs/bin/env python3.6
# from user import User
# from credential import Credential


# def create_user(user_name,user_login):
#     '''
#     Function to create new user
#     '''
#     new_user = User(user_name,user_login)
#     return new_user

# def save_user(user):
#     '''
#     Function to saver new user
#     '''
#     user.save_user()

# def create_credential(credential_name,user_name,password):
#     '''
#     Function that creates new credentials for a given user account
#     '''
#     new_credential =Credential(credential_name,user_name,password)
#     return new_credential

# def delete_credential(credential):
#     '''
#     function to delete credential
#     '''
#     credential.delete_credential()

# def save_credential(credential):
#     """
#     Function to save Credentials to the credentials list
#     """
#     credential.save_credential()

# def display_credential():
#     """
#     Function that returns all the saved credential.
#     """
#     return Credential.display_credential()

# def find_credential(name):
#     '''
#     function for finding credential
#     '''
    
#     return Credential.find_by_name(name) 

# def generate_Password():
#     '''
#     generates a random password for credential
#     '''
#     generatedPassword= Credential.genarate_password()
#     return generatedPassword

# def main():
#     print("Hello Welcome to your Pass Word Locker. What is your name?")
#     user_name = input()
#     print(f"Hello {user_name}, sign up to Pass Word Locker to create an account.")
#     print('\n')
#     while True:
#         print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n ex ->exit Pass Word Locker. ")
#         short_code = input().lower()
#         if short_code == 'su':
#             print("Create a Pass Word Locker Account")
#             print("_"*100)
#             account_name = input('user_name:')
#             print ('\n')
#             pwd = input('user_login : ')
#             print ('\n')
#             save_user(create_user(user_name,pwd,)) 
#             print ('\n')
#             print(f"A New {user_name} Account with the user name  {user_name} has been created.")
#             print(f"You can now login to your {account_name} account using your password.")
#             print ('\n')
#         elif short_code == 'ln':
#                     print("Enter your User_name and your User_login to log in:")
#                     username = input("user_name: ")
#                     userlogin = input ("user_login: ")
#                     # login_user(user_name,user_login)
#                     if (username == "Alex123" and userlogin =="123alex"):
#                         print(f"Hello {username}, Welcome back to Password Locker")
#                         print('\n')
#                     else:
#                         print("Credentials do not match existing user")
#                     while True:
#                             print('''
#                             Use these short codes:
#                             CA -> Create new credential.
#                             DC -> Display your credential list
#                             DEL -> Delete credential
#                             EX ->Log out your credential account.''')
#                             short_code = input().upper()
#                             if short_code == "CA":
#                                 print("Create new credential")
#                                 print('_' * 20)
#                                 credential_name = input('Credential name:')
#                                 print('\n')
#                                 user_name = input(f"{credential_name} user name:")
#                                 print('\n')
#                                 print('*' * 20)
#                                 pwd = input(f"{credential_name} password:")
#                                 save_credential(create_credential(credential_name,user_name,pwd))
#                                 print('\n')
#                                 print(f"A New {credential_name} Account with the user name  {user_name} has been created.")
#                                 print ('\n')
#                             elif short_code == 'DC':
#                                 if display_credential():
#                                         print("Here is your credential")
#                                         print('\n')
#                                         for credential in display_credential():
#                                             print(f"Credential name:{credential.credential_name}  User name: {credential.user_name} Password:{credential.password}")
#                                             print('\n')
#                                 else:
#                                     print('\n')
#                                     print("You don't seem to have created any account yet")
#                                     print('\n')
#                             elif short_code =="DEL":
#                                 print('\n')
#                                 print("Enter the account name you want to delete")
#                                 name = input().lower()
#                                 if find_credential(name):
#                                     search_credential = find_credential(name)
#                                     print("_"*50)
#                                     search_credential.delete_credential()
#                                     print('\n')
#                                     print(f"Your stored credentials for : {search_credential.credential_name} successfully deleted!!!")
#                                     print('\n')
#                             elif short_code == "EX":
#                                 print('\n')
#                                 print(f"You have logged out your {account_name} account")
#                                 print('\n')
#                                 break  
#                     else:
#                         print("Credentials do not match existing user")           
#         else:
#             print('\n')
#             print("WRONG PASSWORD!! PLEASE ENTER CORRECT PASSWORD TO LOGIN")
#             print('\n')
#             print('\n')

# if __name__ == '__main__':
#     main()
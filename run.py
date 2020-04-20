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
    user.save_user():

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
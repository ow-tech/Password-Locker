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

#!/urs/bin/env python3.6
from user import User
from credential import Credential


def create_user(user_name,user_login):
    new_user = User(user_name,user_login)
    return new_user
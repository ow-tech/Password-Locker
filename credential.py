import random
import string
import pyperclip

class Credential:

    credential_list = []
    '''
    class that generates new instances of credentials
    '''
    def __init__(self,credential_name, usr_name,password):
        self.credential_name = credential_name
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        '''
        method that saves new credential
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        method that deletes credential
        '''
        Credential.credential_list.remove(self)
    

    @classmethod
    def find_by_name(cls,name):
        for credential in cls.credential_list:
            if credential.password == name:
                return credential

        return False

    @classmethod
    def display_credential(cls):
        '''
        method that returns all of the credentials in credential list
        '''
        return cls.credential_list 

    def genarate_password(stringLength=8):
        '''
        method for randomly generating a password
        '''
        generatedPassword = string.asscii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(generatedPassword)for i in range(stringLength))



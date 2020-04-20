class Credential:

    credential_list = []
    '''
    class that generates new instances of credentials
    '''
    def __init__(self,credential_name, usr_name,password):
        self.credential_name = credential_name
        self.usr_name = usr_name
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
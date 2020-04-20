class Credential:
    '''
    class that generates new instances of credentials
    '''
    def __init__(self,credential_name, usr_name,password):
        self.credential_name = credential_name
        self.usr_name = usr_name
        self.password = password
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
        Credential.credential_list.append(self)

    def test_save_multiple_credentials(self):
            '''
            test that checks if multiple user objects are saved
            '''
            self.new_credential.save_credential()
            test_credential=Credential("Intagram","Kim123","123kim") #new Credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

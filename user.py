class User:
    ''''
    Class that authenticates User
    '''

    user_list= []
    def __init__(self,user_name,user_login):
        self.user_name = user_name
        self.user_login = user_login
    
    def save_user(self):

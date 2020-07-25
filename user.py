# class User:

#     user_list = []
#     ''''
#     Class that authenticates User
#     '''

#     user_list= []
#     def __init__(self,user_name,user_login):
#         self.user_name = user_name
#         self.user_login = user_login
    
#     def save_user(self):
#         User.user_list.append(self)
class User:
    '''
    class that authenticates User
    '''

    #  a list to store new user objects
    user_list = []
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        User.user_list.append(self)

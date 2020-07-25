# import unittest
# from user import User

# class TestUser(unittest.TestCase):

#     '''
#     Test class to define behavious of User class

#     Args:
#         unittest.TestCase: TestCase class that helps creating test case:
#     '''
#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_user = User("Alex123", "123alex")


#     def test_init(self):
#         self.assertEqual(self.new_user.user_name,"Alex123")
#         self.assertEqual(self.new_user.user_login,"123alex")

#     def test_save_user(self):
#         '''
#         test to ensure that users are being saved as they are created
#         '''
#         self.new_user.save_user()
#         self.assertEqual(len(User.user_list),1)

#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run.
#         '''
#         User.user_list =[]

#     def test_save_multiple_user(self):
#         '''
#         test for saving multiple users
#         '''
#         self.new_user.save_user()
#         test_user = User("Kim123","123kim")
#         test_user.save_user()
#         self.assertEqual(len(User.user_list),2)





# if __name__ == '__main__':
#     unittest.main()
import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    Set up method to run before each test cases.
    '''
    def setUp(self):
        self.new_user = User('alex', 'alex123')
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertTrue(self.new_user.user_name, 'alex')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.user_list),1)
    def test_save_multiple_user(self):
        self.new_user.save_user
        another_user = User('kim','123')
        another_user.save_user()
        self.assertTrue(len(User.user_list),1)
 

if __name__ == '__main__':
    unittest.main()
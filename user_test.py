import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class to define behavious of User class

    Args:
        unittest.TestCase: TestCase class that helps creating test case:
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
         self.new_user = User("Alex123", "123alex")


    def test_init(self):
        self.assertEqual(self.new_user.user_name,"Alex123")
        self.assertEqual(self.new_user.user_login,"123alex")
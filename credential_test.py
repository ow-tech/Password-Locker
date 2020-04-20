import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
        '''
    Test class to define behavious of Credential class

    Args:
        unittest.TestCase: TestCase class that helps creating test case:
    '''

        def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_credential= Credential("Instagram","Alex123","123alex")

        def test_init(self):
            '''
            test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_credential.credential_name,"Instagram")
            self.assertEqual(self.new_credential.usr_name,"Alex123")
            self.assertEqual(self.new_credential.password,"123alex")
        
        def test_save_credential(self):
            '''
            test case to ensure user saves his/her logins

            '''
            self.new_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),1)
if __name__ == '__main__':
    unittest.main()
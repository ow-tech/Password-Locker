import unittest
from credential import Credential
import pyperclip

# class TestCredential(unittest.TestCase):
#         '''
#     Test class to define behavious of Credential class

#     Args:
#         unittest.TestCase: TestCase class that helps creating test case:
#     '''

#         def setUp(self):
#             '''
#             Set up method to run before each test cases.
#             '''
#             self.new_credential= Credential("Instagram","Alex123","123alex")

#         def test_init(self):
#             '''
#             test case to test if the object is initialized properly
#             '''
#             self.assertEqual(self.new_credential.credential_name,"Instagram")
#             self.assertEqual(self.new_credential.usr_name,"Alex123")
#             self.assertEqual(self.new_credential.password,"123alex")
        
#         def test_save_credential(self):
#             '''
#             test case to ensure user saves his/her logins

#             '''
#             self.new_credential.save_credential()
#             self.assertEqual(len(Credential.credential_list),1)


#         def tearDown(self):
            
#             Credential.credential_list = []    

#         def test_save_multiple_credentials(self):
#                 '''
#                 test that checks if multiple user objects are saved
#                 '''
#                 self.new_credential.save_credential()
#                 test_credential=Credential("Intagram","Kim123","123kim") #new Credential
#                 test_credential.save_credential()
#                 self.assertEqual(len(Credential.credential_list),2)

#         def test_delete_credential(self):

#             self.new_credential.save_credential()
#             test_credential = Credential("Intagram","Kim123","123kim")
#             test_credential.save_credential()


#             self.new_credential.delete_credential()
#             self.assertEqual(len(Credential.credential_list),1)

#         def test_find_credential_by_credential_name(self):

#             self.new_credential.save_credential()
#             test_credential = Credential("Intagram","Kim123","123kim")
#             test_credential.save_credential()

#             found_credential = Credential.find_by_name("123kim")
#             self.assertEqual(found_credential.password,test_credential.password)

#         def test_display_all_saved_credentials(self):
#             '''
#             test for displaying saved credential
#             '''
#             self.assertEqual(Credential.display_credential(),Credential.credential_list)



class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential('Instagram','alexinsta','alex1234565')
    def tearDown(sel):
        Credential.credential_list = []
    def test_init(self):
        self.assertTrue(self.new_credential.account_name, 'Instagram')
    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertTrue(len(Credential.credential_list), 1)
    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()
        self.another_credential = Credential('Twitter', 'TwitterAlex','Twitterpassword')
        self.another_credential.save_credential()
        self.assertTrue(len(Credential.credential_list),2)
    def test_credential_exists(self):
        self.new_credential.save_credential()
        test_credential = Credential('Twitter', 'TwitterAlex','Twitterpassword')
        test_credential.save_credential()
        credential_exists = Credential.find_by_name('Twitter')
        self.assertTrue(credential_exists)
    def test_delete_credential(self):
        self. new_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),0)
    def test_display_all_credentials(self):
        self.assertEqual (Credential.display_all_credentials(),Credential.credential_list)
    def test_copy_credential_password(self):
        self.new_credential.save_credential()
        Credential.copy_password('Instagram')
        self.assertTrue(self.new_credential.account_password, pyperclip.paste())
    def generate_password(stringLength=8):
        account_password = 



if __name__ == '__main__':
    unittest.main()
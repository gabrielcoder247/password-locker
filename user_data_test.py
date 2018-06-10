import unittest # Importing the unittest module
from user_data import User# Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gabriel","Nwachukwu","moringa123") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Gabriel")
        self.assertEqual(self.new_user.last_name,"Nwachukwu")
        self.assertEqual(self.new_user.password,"moringa123")

    def test_save_user(self):
        '''
        test_user_contact test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.users_list),1) 

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.users_list = []

# other test cases here
    def test_save_user(self):
            '''
            test_save_user to check if we can save user
            objects to our User_list
            '''
            self.new_user.save_user()
            test_user = User("Gabriel","Nwachukwu","moringa123") # new contact
            test_user.save_user()
            self.assertEqual(len(User.users_list),2)        

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Gabriel','Nwachukwu','moringa123')
		self.new_user.save_user()
		user2 = User('peter','okoye','nigeria123')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

    def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential('peter','Facebook','okoye','nigeria123')    
           

if __name__ == '__main__':
    unittest.main()
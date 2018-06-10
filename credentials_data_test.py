import unittest # Importing the unittest module
from credentials_data import Credential # Importing the credential class
from user_data import User # Importing the user class

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
		user2 = User('Roland','Nwachukwu','yola123')
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
		self.new_credential = Credential('Mary','Facebook','maryjoe','nairobi123')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'Mary')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'maryjoe')
		self.assertEqual(self.new_credential.password,'nairobi123')

def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Jane','Twitter','maryjoe','nairobi123')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)            

if __name__ == '__main__':
    unittest.main()        
    

import unittest # Importing the unittest module
from credntials_data import Credentials # Importing the contact class

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
		self.new_user = User('Gabriel','Nwachukwu,'moringa123')
		self.new_user.save_user()
		user2 = User('Roland','Nwachukwu,'yola123')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

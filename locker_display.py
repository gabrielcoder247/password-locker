import pyperclip
from credentials_data import Credential # Importing the credential class
from user_data import User # Importing the user class

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user
    
def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)    
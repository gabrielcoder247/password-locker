# import pyperclip
# from user_data import User
class User:
    """
    Class that generates new instances of user.
    """
    users_list = [] # Empty user list
    
    def __init__(self,first_name,last_name,password):
        # docstring removed for simplicity
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

        # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.users_list.append(self)
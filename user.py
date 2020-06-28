class User:

    """
    class that generates new instance of the user
    """
    user_list = []

    def __init__(self,user_name,password):
        self.user.name = user_name
        self.password = password

    def save_user (self):

        """
        save user method saves a  new user to the user list 
        """
        User.user_list.append(self)

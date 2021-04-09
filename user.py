class User:

    users_list = []

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def add_user(self):
        User.users_list.append(self)
        return User.users_list

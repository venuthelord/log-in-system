class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def login(user_list, username, password):
    for user in user_list:
        if user.username == username and user.password == password:
            return True
    return False
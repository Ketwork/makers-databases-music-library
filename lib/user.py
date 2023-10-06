class User:
    def __init__(self,id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __eq__(self, other):
            return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email})"
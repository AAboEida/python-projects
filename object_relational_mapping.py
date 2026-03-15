"""Object-Relational Mapping (ORM) is a programming technique that
allows developers to interact with databases using object-oriented programming languages
"""


class User:
    """A simple User class to demonstrate ORM-like behavior"""

    db = {}
    id_counter = 1

    def __init__(self, name, email):
        """Initialize a new User instance"""
        self.id = None
        self.name = name
        self.email = email
    def save(self):
        """Save the User instance """
        if self.id is None:
            self.id = User.id_counter
            User.id_counter += 1
            User.db[self.id] = self
            return print(f"User created with id: {self.id}")
        return print("User already exists. Use update() to modify the user.")

    @classmethod
    def read(cls, user_id):
        """Read a User instance  by user_id"""
        return cls.db.get(user_id)

    @classmethod
    def read_all(cls):
        """Read all User instances """
        user_list = list(cls.db.values())
        if not user_list:
            return "No users found"
        return user_list

    @classmethod
    def delete(cls, user_id):
        '''Delete a User instance by user_id'''
        removed = cls.db.pop(user_id, None)
        if removed:
            return print("User deleted")
        return print("User not found")

    @classmethod
    def update(cls, user_id, name=None, email=None):
        """Update a User instance by user_id"""
        user = cls.db.get(user_id)
        if name and email:
            user.name = name
            user.email = email
            return print("User updated successfully")
        if name:
            user.name = name
            return print("User name updated successfully")
        if email:
            user.email = email
            return print("User email updated successfully")
        return print("No updates provided")

    def __repr__(self):
        """Return a string representation of the User instance"""
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


user1 = User("Ahmed", "ahmed@gmail.com")
user1.save()
user1 = User.read(user1.id)
print(user1.name)  # Output: Ahmed
User.update(user1.id, name="Ahmed Mohamed")
User.delete(user1.id)
print(User.read_all())  # Output: [] (empty list, since the user has been deleted)
User.delete(100)  # Output: User not found

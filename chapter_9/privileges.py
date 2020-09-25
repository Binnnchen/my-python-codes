from user import User

class Privileges():
    """权限类"""

    def __init__(self):
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
        ]

    def show_privileges(self):
        print("\nRoots: ")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(
            self, first_name,
            last_name, age, location):
        super().__init__(
            first_name,
            last_name,
            age, location)
        self.privileges = Privileges()



class User():

    def __init__(
            self, first_name,
            last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print("\nName: " + full_name.title())
        print("Age: " + str(self.age))
        print("Location: " + self.location.title())

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Happy to see you, " + full_name.title() + " !")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将login次数重置为0"""
        self.login_attempts = 0

    def read_login_attempts(self):
        print("\nLogin attempts: " + str(self.login_attempts))



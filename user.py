class User():

    def __init__(self, first_name, last_name, date_born):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.date_born = date_born
        self.login_attempts = 0

    def describe_user(self):
        print(f'Username - {self.first_name} {self.last_name}. Date of born - {self.date_born}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


myself = User('nikita', 'reznikov', '10.11.1994')
wife = User('jane', 'spirina', '23.04.1998')
friend = User('johnny', 'rudenko', '8.08.1995')

myself.describe_user()
myself.greet_user()
print(myself.login_attempts)
myself.increment_login_attempts()
myself.increment_login_attempts()
myself.increment_login_attempts()
print(myself.login_attempts)
myself.increment_login_attempts()
myself.increment_login_attempts()
print(myself.login_attempts)
myself.reset_login_attempts()
print(myself.login_attempts)
#wife.describe_user()
#wife.greet_user()

#friend.describe_user()
#friend.greet_user()

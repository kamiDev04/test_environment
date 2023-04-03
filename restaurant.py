class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.capitalize()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Our restaurant where you can eat {self.cuisine_type} food is called "{self.restaurant_name}"')

    def open_restaraunt(self):
        print(f'Restaraunt "{self.restaurant_name}" is open!')

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, visit):
        self.number_served += visit

my_restaraunt = Restaurant('pinneberg', 'german')
#restaurant1 = Restaurant('kikis', 'asian')
#restaurant2 = Restaurant('popkins', 'american')

my_restaraunt.describe_restaurant()
#restaurant1.describe_restaurant()
#restaurant2.describe_restaurant()

print(my_restaraunt.number_served)
my_restaraunt.set_number_served(40)
print(my_restaraunt.number_served)
my_restaraunt.increment_number_served(200)
print(my_restaraunt.number_served)


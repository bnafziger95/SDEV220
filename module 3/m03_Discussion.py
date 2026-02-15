# Brooke Nafziger
# Module 3 - Disussion Code Review

# define user class
class User:
    def __init__(self, first_name, last_name, age, gender, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.city = city

# method to describe user 
    def describe_user(self):
        print(f"User Profile: \nName:{self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nCity: {self.city}")

# method to greet user
    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome back!\n")

# create instances of user class
user1 = User("Ella", "Bella", 30, "Female", "Detroit")
user2 = User("John", "Doe", 25, "Male", "Indianapolis")
user3 = User("Frank", "Johnson", 20, "Male", "Chicago")
user4 = User("Emily", "Smith", 40, "Female", "Denver")
user5 = User("James", "Bond", 35, "Male", "London")

# call methods for each user
users = [user1, user2, user3, user4, user5]

for user in users:
    user.describe_user()
    user.greet_user()

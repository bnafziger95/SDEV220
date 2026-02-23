# Brooke Nafziger
# m04 - functions and classes

# write python app that has multipe classes
# superclass: vehicle
    # attribute for vehicle type
# subclass: automobile
    # attributes: year, make, model, doors, roof
# app to accept user input for car
# app store car into the vehicle type
# app ask for user input for car attributes
# output the data in a readable format
    # Vehicle type:
    # Year:
    # Make:
    # Model:
    # Number of doors:
    # Type of roof:

# create superclass for vehicle
class Vehicle:
    def __init__ (self, vehicle_type):
        self.vehicle_type = vehicle_type

# create subclass for car
class Automobile(Vehicle):
    def __init__ (self, vehicle_type, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# main application
def get_car_info():
        print("Enter vehicle information:\n")
        
        # create function to ask user for input
        vehicle_type = input("Enter the vehicle type: ")
        year = input("Enter the year: ")
        make = input("Enter the make: ")
        model = input("Enter the model: ")
        doors = input("Enter the number of doors: ")
        roof = input("Enter the type of roof: ")
        car = Automobile(vehicle_type, year, make, model, doors, roof)
        
        # create function to output data in readable format
        print(f"Vehicle type: {car.vehicle_type}")
        print(f"Year: {car.year}")
        print(f"Make: {car.make}")
        print(f"Model: {car.model}")
        print(f"Number of doors: {car.doors}")
        print(f"Type of roof: {car.roof}")

# run program
get_car_info()

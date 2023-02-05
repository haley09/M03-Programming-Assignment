class Vehicle():
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __int__(self, year, make, model, doors, roof, vehicleType = "car"):
        Vehicle().__init__(self, vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

car = Automobile(

    year = input("What is the year of the vehicle? "),

    make = input("What is the make of the vehicle? "),

    model = input("What is the model of the vehicle? "),

    doors = input("How many doors does the vehicle have? (2 or 4) "),

    roof = input("Is the roof of the vehicle solid or sun roof? ")
)

print("Vehicle type: " + car.vehicleType)
print("Year: " + car.year)
print("Make: " + car.make)
print("Model: " + car.model)
print("Number of doors: " + car.doors)
print("Type of roof: " + car.roof)
class Car:
    def __init__(self, model, year):
        self.__model = model  # Private attribute
        self.year = year

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

# Creating an object
my_car = Car("Toyota", 2020)

print(my_car.get_model())  # Output: Toyota
my_car.set_model("Honda")
print(my_car.get_model())  # Output: Honda

my_car.year = 2024
print(my_car.year)  # Output: Honda

my_car.__model = "A" #doesnot fail but value is also not updated
print(my_car.get_model())

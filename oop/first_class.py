class Dog:
    """
    This is a dog class
    """
    name = "First Dog"

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def dog_details(self):
        print(self.name,self.age)


dog = Dog("rocky", 4)

print(dog.__doc__)

print(dog.dog_details())
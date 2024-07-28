class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof Woof
print(cat.speak())  # Output: Whiskers says Meow

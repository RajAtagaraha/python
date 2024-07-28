x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")



# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Counting down from 5
i = 5
while i > 0:
    print(i)
    i -= 1

# Using break to exit a loop
for i in range(5):
    if i == 3:
        break
    print(i)

# Using continue to skip an iteration
for i in range(5):
    if i == 3:
        continue
    print(i)


def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object of the Person class
person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

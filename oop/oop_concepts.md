# Object Oriented Programming Concepts 

What is Object-Oriented Programming ?

    Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code to manipulate that data. 
    Key concepts include classes, objects, inheritance, and polymorphism.

What are classes?
    
       Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
       
What is an object?
    
      Object: An instance of a class.
      
Give example of a class?

    class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    # Creating objects
    my_dog = Dog("Buddy", 5)
    your_dog = Dog("Lucy", 3)
    
    # Accessing attributes and methods
    print(my_dog.description())  # Output: Buddy is 5 years old
    print(your_dog.speak("Woof Woof"))  # Output: Lucy says Woof Woof

Explain Inheritance:
    
    Inheritance is a way to form new classes using classes that have already been defined. 
    It helps in reusing the code and establishing a relationship between classes.

Explain Polymorphism:

    Polymorphism allows us to define methods in the child class with the same name as defined in their parent class. 
    It means having many forms.
    Overloading and Overridding                 

Explain Encapsulation:
    
    Encapsulation restricts direct access to some of an object's components, which can prevent the accidental modification of data from external objects.
    Private variables are created using double underscores (__).
    
What is the difference between a class attribute and an instance attribute?
    
        Class attribute: Shared by all instances of the class.
        Instance attribute: Unique to each instance.
        
Explain the __init__ method. Why is it used?
            
        The __init__ method is a special method called a constructor. It is automatically called when an object is instantiated and is used to initialize the object's attributes.

What is inheritance? Provide an example?
    
        Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
        
         class Parent:
          def __init__(self, name):
            self.name = name

         class Child(Parent):
            def __init__(self, name, age):
                super().__init__(name) # called a super class from child class
                self.age = age
      
What is the super() function?

    The super() function returns a temporary object of the superclass that allows you to call its methods.

What is polymorphism? How is it implemented in Python?
    
        Polymorphism means having many forms. It allows methods to be used in different ways
        class Animal:
            def speak(self):
                pass
    
        class Dog(Animal):
            def speak(self):
                return "Woof"
        
        class Cat(Animal):
            def speak(self):
                return "Meow"

What is method overriding? 
    
       Method overriding allows a child class to provide a specific implementation of a method already defined in its parent class.
       

What is encapsulation? How is it achieved in Python?
    
        Encapsulation restricts access to methods and variables. This is achieved by private attributes using double underscores (__).

Explain the difference between public, protected, and private attributes.

      Public attributes: Accessible from outside the class.
      Protected attributes: Accessible within the class and its subclasses.
      Private attributes: Accessible only within the class.
      
What is multiple inheritance? Provide an example
    
    Multiple inheritance is when a class is derived from more than one base class
    
    class Parent1:
        pass

    class Parent2:
        pass
    
    class Child(Parent1, Parent2):
        pass

How do you implement a class method and a static method?
    
    class MyClass:
        @classmethod
        def class_method(cls):
            pass

        @staticmethod
        def static_method():
            pass
            
What are dunder/magic methods? Provide examples

              
    Dunder methods are special methods that start and end with double underscores. 
    Examples include __init__, __str__, and __repr__.
    
    class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"

How can you implement method chaining in Python?
    
    Method chaining is achieved by returning self in the methods.
           
    class MyClass:
        def method1(self):
            # Do something
            return self

        def method2(self):
            # Do something
            return self

    obj = MyClass().method1().method2()
          
What is the @property decorator? How do you use it?
    
    The @property decorator allows you to define methods that can be accessed like attributes.
    
    class MyClass:
        def __init__(self, value):
            self._value = value
    
        @property
        def value(self):
            return self._value
    
        @value.setter
        def value(self, value):
            self._value = value
    
        obj = MyClass(10)
        print(obj.value)  # Accessing the property
        obj.value = 20  # Setting the property

            
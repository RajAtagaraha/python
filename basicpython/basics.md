What are the different data types in Python? Provide examples.

    numeric - 
        int, float, complex
    
    boolean -
        bool 
    
    sequence type -    
        string,  list, tuple
       
    mapping type - 
        dict
     
    set type 
        set , fronzeset 
     
    binary types 
        bytes, bytearray, memoryview
        
     
     
How does Python handle type conversion? Can you provide examples of implicit and explicit type conversion?

        x = 10
        y = 2.5
        z = x + y  # x is implicitly converted to float
        print(z) 
        
        x = 10
        y = "20"
        z = x + int(y)  # y is explicitly converted to int
        print(z)  # Output: 30

What is the difference between a list and a tuple? When would you use one over the other?

        List: Mutable, can be changed after creation
        Tuple : Immutable, cannot be changed after creation
       

How do you create a dictionary in Python? What are some common operations you can perform on a dictionary?
    
        my_dict = {"name": "Alice", "age": 25}
        # Accessing values
        print(my_dict["name"])  # Output: Alice
        # Adding a new key-value pair
        my_dict["gender"] = "Female"
        # Removing a key-value pair
        my_dict.pop("age")


What are sets in Python? How are they different from lists and tuples?
        
        Sets are unordered collections of unique elements.
        my_set = {1, 2, 3, 3}  # Duplicate values are removed
        print(my_set)  # Output: {1, 2, 3}
        
        Difference from lists and tuples:
            Lists are ordered and allow duplicate values.
            Tuples are ordered and immutable.
            
    Tuples are fixed size in nature whereas lists are dynamic.
        In other words, a tuple is immutable whereas a list is mutable.
        
        You can't add elements to a tuple. Tuples have no append or extend method.
        You can't remove elements from a tuple. Tuples have no remove or pop method.
        You can find elements in a tuple, since this doesn’t change the tuple.
        You can also use the in operator to check if an element exists in the tuple.     
        
    Tuples are faster than lists. If you're defining a constant set of values and all you're ever 
    going to do with it is iterate through it, use a tuple instead of a list.   
    
    It makes your code safer if you “write-protect” data that does not need to be changed. Using a tuple instead of a list is like having an implied assert statement that this data is constant, and that special thought (and a specific function) is required to override that.

    Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples). 
    Lists can never be used as dictionary keys, because lists are mutable.    

How do you check the type of a variable in Python?
    
        x = 10
        print(type(x))  # Output: <class 'int'>

Explain the difference between mutable and immutable types in Python. Provide examples.
    
        
        Mutable: Can be changed after creation. Example: list, dict, set.
        Immutable: Cannot be changed after creation. Example: int, float, str, tuple
                
        
       
How do you handle binary data in Python? What data types are used for this purpose?

        Bytes
            byte_data = b"hello"
        
        Bytearray
            byte_array = bytearray(5)

        mem_view
            mem_view = memoryview(byte_data)

What is the difference between == and is in Python? Provide examples.
    
        == checks for value equality.
        is checks for identity (whether both operands refer to the same object)
        a = [1, 2, 3]
        b = [1, 2, 3]
        print(a == b)  # Output: True
        print(a is b)  # Output: False

            
Explain how Python handles boolean values. How can you use booleans in control flow statements?
    
        
        x = True
        if x:
            print("x is True")  # Output: x is True

Explain the concept of interning in Python and how it applies to strings.

    String interning is a method of storing only one copy of each distinct string value, which must be immutable.
    
    a = "hello"
    b = "hello"
    print(a is b)  # Output: True (due to interning for small strings)
    c = "hello world"
    d = "hello world"
    print(c is d)  # Output: False (interning is not guaranteed for larger strings)


How do you create a multi-level dictionary in Python? How can you safely access a deeply nested key?

    nested_dict = {"level1": {"level2": {"level3": "value"}}}
    # Safe access using get method
    level3_value = nested_dict.get("level1", {}).get("level2", {}).get("level3")
    print(level3_value)  # Output: value


What is the difference between shallow copy and deep copy in Python? Provide examples.

    Shallo copy 
        import copy
        original_list = [1, [2, 3]]
        shallow_copy = copy.copy(original_list)
        shallow_copy[1][0] = 99
        print(original_list)  # Output: [1, [99, 3]]
     
    Deep Copy   
        import copy
        original_list = [1, [2, 3]]
        deep_copy = copy.deepcopy(original_list)
        deep_copy[1][0] = 99
        print(original_list)  # Output: [1, [2, 3]]


Explain the concept of hashability. Which built-in data types are hashable and which are not?

    Hashable objects have a hash value that does not change during their lifetime (e.g., int, float, str, tuple).
    Non-hashable objects are mutable (e.g., list, dict, set)
    
    hashable_example = (1, 2, 3)
    print(hash(hashable_example))  # Output: hash value
    non_hashable_example = [1, 2, 3] # print(hash(non_hashable_example))  # This will raise a TypeError

    

Describe how Python's memory management works for immutable and mutable objects.

    Immutable objects (e.g., int, str) are stored in a way that allows reuse.

    Mutable objects (e.g., list, dict) have separate memory allocations.
    
    a = 10
    b = 10
    print(a is b)  # Output: True (same memory location)
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(list1 is list2)  # Output: False (different memory locations)
    

What are Python's built-in functions for working with different data types? Provide examples of map(), filter(), and reduce().
    
    map(): Applies a function to all items in an input list

    numbers = [1, 2, 3, 4]
    squares = map(lambda x: x**2, numbers)
    print(list(squares))  # Output: [1, 4, 9, 16]

    filter()
    numbers = [1, 2, 3, 4]
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    print(list(even_numbers))  # Output: [2, 4]
    
    reduce(): Applies a rolling computation to sequential pairs of values in a list

    from functools import reduce
    numbers = [1, 2, 3, 4]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)  # Output: 24

How can you implement a switch-case-like statement in Python, which doesn't have a native switch-case construct?

    def switch_case(value):
    switcher = {
        1: "one",
        2: "two",
        3: "three",
    }
    return switcher.get(value, "Invalid value")
   
    print(switch_case(2))  # Output: two
    print(switch_case(5))  # Output: Invalid value
    
    
What is the significance of the __slots__ attribute in classes? How does it affect memory usage and performance?
    
    Restricts class attributes to save memory
    
    class MyClass:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age
    obj = MyClass("Alice", 30)
    #obj.new_attr = "test"  # This will raise an AttributeError
    
    
Discuss how to create and manipulate frozensets. Why and when would you use a frozenset instead of a regular set?
    
    Frozensets are immutable sets
    my_set = {1, 2, 3}
    my_frozenset = frozenset(my_set)
    # my_frozenset.add(4)  # This will raise an AttributeError
    print(my_frozenset)  # Output: frozenset({1, 2, 3})

Defining Functions

    Functions are blocks of code that perform a specific task. They help in organizing code, reusability, and reducing redundancy.
    
    def function_name(parameters):
    """docstring"""
    # Function body
    return value

    Eg;
       def greet(name):
    """This function greets the person whose name is passed as an argument."""
    return f"Hello, {name}!"
    print(greet("Alice"))  # Output: Hello, Alice!
    
What are modules in Python?

    Modules are files containing Python code (variables, functions, classes) that can be imported and used in other Python programs.
     eg;
     import module: 
         import math
         print(math.sqrt(16))  # Output: 4.0

    import specefic function from a module         
    from math import sqrt, pi
        print(sqrt(16))  # Output: 4.0
        print(pi)        # Output: 3.141592653589793

    Importing with an Alias:
        import numpy as np

        array = np.array([1, 2, 3, 4])
        print(array)  # Output: [1 2 3 4]
        
Mention few Python built in function 
        
       Python has numerous built-in functions that are always available.
        # len(): Returns the length of an object
        print(len("Hello"))  # Output: 5
        
        # type(): Returns the type of an object
        print(type(3.14))    # Output: <class 'float'>
        
        # input(): Reads input from the user
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
        
        # print(): Prints the specified message to the screen
        print("Hello, World!")  # Output: Hello, World!
        
        # range(): Returns a sequence of numbers
        for i in range(5):
            print(i)  # Output: 0 1 2 3 4
        
        # sum(): Sums the items of an iterable
        print(sum([1, 2, 3, 4]))  # Output: 10
        
        # min() and max(): Returns the smallest and largest item
        print(min(1, 2, 3, 4))  # Output: 1
        print(max(1, 2, 3, 4))  # Output: 4

What are lambda functions and how to use it?

    In Python, lambda functions are anonymous, small, and single-expression functions. They are also known as anonymous functions because they are defined without a name.
    # Lambda function to add 10 to a number
    add_ten = lambda x: x + 10
    print(add_ten(5))  # Output: 15
    
    # Lambda function to multiply two numbers
    multiply = lambda x, y: x * y
    print(multiply(2, 3))  # Output: 6
       
       Use Cases:
    Short, one-time use functions: Lambda functions are great for defining simple functions that you need to use only once.
    Higher-order functions: Lambda functions are often used as arguments to higher-order functions like map(), filter(), and reduce().
    Sorting: Lambda functions can be used to define custom sorting keys.
    Benefits:
    Concise: Lambda functions allow you to write shorter, more readable code.
    Inline: You can define lambda functions directly where you need them, eliminating the need for separate function definitions.
    Functional programming: Lambda functions encourage a functional programming style, which can lead to cleaner and more maintainable code.
    Limitations:
    Single expression:
    Lambda functions can only contain a single expression, which limits their complexity.
    Readability:
    For more complex logic, named functions are often easier to read and understand.

What are higher-order functions? Give an example using Python built-in functions.

    A higher-order function is a function that takes another function as an argument or returns a function as a result.
    
    def apply_func(func, value):
        return func(value)

    print(apply_func(lambda x: x + 1, 10))  # Output: 11

What are decorators in Python? Provide an example.
    Decorators are a way to modify the behavior of a function or method. They are applied using the @decorator syntax.
    
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")
    
    say_hello()
    # Output:
    # Something is happening before the function is called.
    # Hello!
    # Something is happening after the function is called.`

Explain the difference between import and from ... import ... statements.

    import module imports the entire module and you have to use module.name to access its components.
    from module import name imports specific components of a module directly into the namespace.     
    
    import math
    print(math.sqrt(16))  # Access using module name
    
    from math import sqrt
    print(sqrt(16))  # Access directly

What are anonymous functions in Python? How are they different from regular functions?
    Anonymous functions are defined using the lambda keyword and are typically used for short, simple operations.
    Regular functions are defined using the def keyword and can contain multiple expressions.
    
    # Anonymous function
    add = lambda x, y: x + y
    print(add(2, 3))  # Output: 5
    
    # Regular function
    def add(x, y):
        return x + y
    
    print(add(2, 3))  # Output: 5

# Questions on Defining Functions
How do you define a function with default arguments in Python? Provide an example.
    
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

        print(greet("Alice"))           # Output: Hello, Alice!
        print(greet("Bob", "Hi"))       # Output: Hi, Bob!

What are keyword arguments in Python? How do they differ from positional arguments?
    
    Keyword arguments are passed by explicitly specifying the parameter names.
    
    def greet(name, greeting):
    return f"{greeting}, {name}!"

    print(greet(name="Alice", greeting="Hello"))  # Output: Hello, Alice!


Explain variable-length arguments in Python functions. Provide examples for both *args and **kwargs.

    def sum_all(*args):
        return sum(args)

    print(sum_all(1, 2, 3, 4))  # Output: 10
    
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    print_info(name="Alice", age=25)
    # Output:
    # name: Alice
    # age: 25

What is a closure in Python? How do you create one?
    
    def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

    closure = outer_function("Hello, World!")
    closure()  # Output: Hello, World!

How do you ensure that a Python function always receives certain arguments as keyword arguments?
    
    def my_function(a, b, *, c):
    return a + b + c

    print(my_function(1, 2, c=3))  # Output: 6
    # print(my_function(1, 2, 3))  # This will raise a TypeError


What is the purpose of the return statement in a function? What happens if you don't use a return statement?
    
    The return statement exits a function and optionally passes back a value.

#Questions on Importing Modules
What are the different ways to import a module in Python?
    
    import math
    from math import sqrt
    import math as m
    from math import *  # Not recommended

How do you handle circular imports in Python?
    
    Circular imports occur when two modules depend on each other. This can often be resolved by rethinking the design or using imports within functions.
    # module1.py
    import module2
    
    def func1():
        module2.func2()
    
    # module2.py
    import module1
    
    def func2():
        module1.func1()

Explain the difference between import module and from module import name. When would you use each?
    
    import math
    print(math.sqrt(16))  # Access using module name
    
    from math import sqrt
    print(sqrt(16))  # Access directly


What is the __name__ attribute in Python modules? How can it be used?
    
    # module.py
    def main():
        print("This is the main function.")
    
    if __name__ == "__main__":
        main()
    # When run directly, prints "This is the main function."
    # When imported, does not run main()


How do you reload a module in Python? In what scenarios might you need to do this?
    
    Reloading a module in Python becomes necessary when you've made changes to the module's source code and want those 
    changes to take effect without restarting the entire Python interpreter. 
    
    import importlib
    import mymodule
    
    importlib.reload(mymodule)

How can you create and use a package in Python?
    A package is a directory with an __init__.py file.
    
    # mypackage/__init__.py

    # mypackage/module.py
    from .module import my_function

What is the use of setup.py File?

    
#Questions on Using Built-in Functions
Explain the use of the map(), filter(), and reduce() functions in Python with examples.
    
    from functools import reduce

        numbers = [1, 2, 3, 4, 5]
        
        squares = map(lambda x: x**2, numbers)
        print(list(squares))  # Output: [1, 4, 9, 16, 25]
        
        even_numbers = filter(lambda x: x % 2 == 0, numbers)
        print(list(even_numbers))  # Output: [2, 4]
        
        product = reduce(lambda x, y: x * y, numbers)
        print(product)  # Output: 120


What is the purpose of the zip() function in Python? Provide an example.
    zip() function allows to combine multiple iterables (e.g., lists, tuples) into a single iterable of tuples
       list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        zipped = zip(list1, list2)
        print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

How does the enumerate() function work in Python? Provide an example.
    
    items = ['apple', 'banana', 'cherry']
    for index, item in enumerate(items):
        print(index, item)
    # Output:
    # 0 apple
    # 1 banana
    # 2 cherry

What is the all() function in Python? How does it differ from the any() function? Provide examples.
    
    numbers = [1, 2, 3, 4, 5]
    print(all(x > 0 for x in numbers))  # Output: True
    print(any(x > 5 for x in numbers))  # Output: False

How can you sort a list of dictionaries by a specific key using a built-in function?

    students = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
    sorted_students = sorted(students, key=lambda x: x['age'])
    print(sorted_students)  # Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]

What is the purpose of the globals() and locals() functions in Python?
    
    The globals() method returns a dictionary containing all global variables and their values. It always returns the module namespace dictionary
    Python locals() provide the same function as globals(), but for methods. Within a method, we call locals()
    x = 10

    def my_function():
        y = 5
        print(locals())  # Output: {'y': 5}
    
    my_function()
    print(globals())  # Output: {'x': 10, ...}


#Data Strucutres in Python 

Explain List:
    
        Lists are ordered, mutable collections of items. They allow duplicate elements and can contain items of different data types.

Explain tuple:

    Tuples are ordered, immutable collections of items. They allow duplicate elements and can contain items of different data types.
    
Explain Dictionary:

    Dictionaries are unordered, mutable collections of key-value pairs. They do not allow duplicate keys.
    
Explain Sets:

    Sets are unordered, mutable collections of unique elements.

What are the advantages of using a set over a list?

          Sets are faster for membership tests (checking if an element is in the set).
          Sets automatically handle duplicates.
          
How do you merge two dictionaries in Python 3.9+?
    
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = dict1 | dict2     
    
What is the time complexity of checking if an element exists in a list versus a set?

    List: O(n)
    Set: O(1)
    
       
#topics dict to list, list to set

#How can you convert a list of tuples into a dictionary?

list_of_tuple = [('a',1),('b',2),('c',3)]

my_dict = dict(list_of_tuple)

print(my_dict)

list_of_tuple = [(1),(2),(3)]

#my_dict = dict(list_of_tuple)#error , tuple should have 2 values

print(my_dict)

list_of_tuple = [(1,5),(2,5),(3,5)]

my_dict = dict(list_of_tuple) #tuple should have 2 values

print(my_dict)

# Explain how to use list comprehension to create a list of squares of even numbers from 0 to 10

list_of_square = [x**2 for x in range(11) if x % 2 == 0] #in range it is exclusive of 11

# How do you create a nested dictionary? Provide an example.

nested_dict = { 'first': {'a':1, 'b':2},
                'second': {'c':3, 'd':4}
                }
print(nested_dict.get('first'))
print(nested_dict.get('first').get('a'))

# How do you create a list of the keys of a dictionary sorted by their values?

my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_keys = sorted(my_dict, key=my_dict.get)
print(sorted_keys)


my_dict = {'b': 3, 'a': 1, 'c': 2}
keys = my_dict.keys()
print(sorted(keys))

#Explain how to use the setdefault() method in dictionaries. Provide an example.

my_dict = {'a': 1}
value = my_dict.setdefault('b', 2)  # Adds 'b' with value 2 if 'b' is not present
print(my_dict)  # Output: {'a': 1, 'b': 2}

my_dict = {'a': 1, 'b':10}
value = my_dict.setdefault('b', 2)  # Adds 'b' with value 2 if 'b' is not present
print(my_dict)  # Output: {'a': 1, 'b': 2}

#How can you find common elements in three lists using sets?
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]
common_elements = set(list1) & set(list2) & set(list3) # & is an intersection in set

#how to convert a list to set

list1 = [1,5,7]

set_s = set(list1)
print(set_s)

#how to remove duplicates from a lit

list1 = [1, 2, 3, 4, 1]
print(list1)
print(set(list1))

#how to remove duplicates from a lit

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

list1.extend(list2)
list1.extend(list3)
print(set(list1))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

list1.append(list2)
list1.append(list3)
print((list1))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

list4 = []
list4.append(list1)
list4.append(list2)
list4.append(list3)

print(list4)

#advance questions on Python DS

#How can you flatten a nested list in Python?

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flattend_list = [item for sublist in nested_list for item in sublist]

print(flattend_list)

#How do you remove duplicate elements from a list while preserving the order?
# if seen already do not add in the set

def remove_duplicates(my_list):
    seen = set() # initialize and empty set and dictionary is emp_dic = {}
    return [x for x in my_list if not (x in seen or seen.add(x))]

my_list = [1, 2, 3, 1, 2, 4]
print(remove_duplicates(my_list))

#How can you find the common elements between two lists?

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))

print(common_elements)
#
#How do you implement a queue using lists?

queue = []

queue.append(1) #enqueue
queue.append(2)

item = queue.pop(0) #dequeue

print(item)
#
#How can you rotate a list by n elements?

def rotate_list(lst, n):
    return lst[n:] + lst[:n]

my_list = [1, 2, 3, 4, 5]
rotated = rotate_list(my_list, 2)
print(rotated)

my_list = [1, 2, 3, 4, 5]
print(my_list[4:] + my_list[:4])

#How can you convert a tuple to a list and vice versa?

my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
my_list = list(my_tuple)

print(type(my_tuple))
print(type(my_list))

#How do you create a tuple with a single element?
single_element_tuple = (1,)

#How can you unpack a tuple into multiple variables?
my_tuple = (1, 2, 3)
a, b, c = my_tuple

#What is tuple concatenation and how do you perform it? + , works for list as well
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)

#How do you iterate over the keys and values of a dictionary simultaneously?
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)

#How can you merge two dictionaries into one?

my_dict1 = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = {'d': 1, 'e': 2, 'f': 3}

merge_dict = {**my_dict1, **my_dict2}
print(merge_dict)

# How do you get the value of a key in a dictionary, providing a default value if the key does not exist?

value_dict = my_dict.get('d',0) # returns 0 if 0 doesn't exists

# How can you sort a dictionary by its keys or values?

sorted_by_keys = dict(sorted(my_dict.items()))
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1])) # needs explanation

print(sorted_by_keys)
print(sorted_by_values)

#How do you remove a key from a dictionary and return its value?
value = my_dict.pop('a', None)  # Returns None if 'a' does not exist
print(value)

#Sets -

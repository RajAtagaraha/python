#How do you create a dictionary in Python?

my_dict  = {'a': 1, 'b': 2, 'c': 3}


#How do you access values in a dictionary?

value = my_dict['a']

#How do you add a key-value pair to a dictionary?

my_dict['d'] = 4

#How do you remove a key-value pair from a dictionary?

del my_dict['b']

#How do you get all keys from a dictionary?

print(my_dict.keys())

#How do you get all values from a dictionary?

print(my_dict.values())

#How do you get all key-value pairs from a dictionary?

print(my_dict.items())

#How do you check if a key exists in a dictionary?

print('a' in my_dict)

#How do you update a dictionary with another dictionary?
my_dict.update({'e':5, 'f':6})

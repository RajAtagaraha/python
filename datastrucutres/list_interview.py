#How do you create a list in Python?

my_list = [1,2,3,4,5,6]

print(my_list)
#How do you add an element to a list?
my_list.append(8)

print(my_list)
#How do you remove an element from a list by value?
my_list.remove(3)  # remove function removes the value from a list by value

print(my_list)
#How do you remove an element from a list by index?

my_list.pop(2) # remove the element at index 2, starting index is 0, hence removes 4, as 3 is already removed above

print(my_list)

#How do you access elements in a list?

print(my_list[0]) # [x] -> x is an index value in the list starting from 0

last_element = my_list[-1] # -1 -> to get last element from the list, or reversing a list

#How do you find the length of a list?

print(len(my_list))

#How do you concatenate two datastrucutres?

list1 = [1,2,3,4]
list2 = [5,6,7,8]

print(list1 + list2)

#How do you check if an element exists in a list?

print( 3 in list1) # true

#What is list comprehension? Provide an example.

squares = [x*2 for x in range(10)] # creates another list with where each value from a list is multiplied by 2
print(squares)


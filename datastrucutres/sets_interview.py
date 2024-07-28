#How do you create a set in Python?

my_set = {1,2,3,4}

#How do you add an element to a set?

my_set.add(5)

#How do you remove an element from a set?

my_set.remove(3) #raise error if not present
my_set.discard(3) # do not raise error if value is not present


#How do you find the length of a set?

print(len(my_set))

#How do you check if an element exists in a set?

exists = 3 in my_set

if exists:
    print("Yes")
else:
    print("No")

#How do you find the union of two sets?
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2

#How do you find the intersection of two sets?

intersection_set = set1 & set2

#How do you find the difference between two sets?

symmetric_difference_set = set1 ^ set2


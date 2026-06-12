#set are unordered collections of unique elements, they are mutable and can be used to perform mathematical set operations like union, intersection, difference, and symmetric difference.

#creating a set
my_set = {1, 2, 3, 4, 5}

#adding elements to a set
my_set.add(6)

#removing elements from a set
my_set.remove(3)

#checking if an element is in a set
print(4 in my_set)  # Output: True

#performing set operations
set_a = {1, 2, 3}

set_b = {3, 4, 5}

#union is the set of all elements that are in either set_a or set_b.    
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

#intersection is the set of elements that are common to both set_a and set_b.
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}

#difference is the set of elements that are in set_a but not in set_b.
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

#symmetric difference is the set of elements that are in either set_a or set_b but not in both.
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


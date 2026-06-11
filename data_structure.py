#inbuild data structure in python examples
#list, tuple, set, dictionary
#list
my_list = [10, 20, 30, 40, 50]   
print("List:", my_list)

#travers on values in list
for i in my_list:
    print(i)  # Output: 10, 20, 30, 40, 50

#traverse on index and values in list
for i in range(0, len(my_list)):
    print(f"Index: {i}, Value: {my_list[i]}")  # Output: Index: 0, Value: 10, etc.



print(my_list[0])  # Output: 10
print(my_list[1:4])  # Output: [20, 30, 40]
my_list.append(60)  # Append 60 to the end of the list
my_list.insert(1, 10)  # Insert 10 at index 1
print("List after insertion:", my_list)


#tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

# set
my_set = {10, 20, 30, 40, 50}    
print("Set:", my_set)

#dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)
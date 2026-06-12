
#dict is used to store data in key value pairs, it is mutable and unordered. 
#creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

#accessing values in a dictionary
print(my_dict['name'])  # Output: Alice
print(my_dict['age'])   # Output: 30
print(my_dict['city'])  # Output: New York

#adding a new key-value pair to the dictionary
my_dict['country'] = 'USA'

#removing a key-value pair from the dictionary
del my_dict['age']  

#checking if a key is in the dictionary
print('name' in my_dict)  # Output: True

#iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")


for i in my_dict.keys():
    #print(i)
    print(my_dict[i], end=' ')

# check key in dict

if 'name' in my_dict:
    print("Key 'name' is in the dictionary.")

for key in my_dict:
    print(key, my_dict[key])   


# key contains in dict
if 'name' in my_dict:
    print("Key 'name' is in the dictionary.")     

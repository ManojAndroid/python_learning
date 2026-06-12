#used tuploes to store multiple items in a single variable , tuples are ordered and unchangeable , they allow duplicate values
tuple=(2,3,4,5,6,7,8,9,10,1,2,1,1,1)

tuple1=("apple","banana","cherry")

#print(tuple)
for i in tuple:
    print(i,end=" ")


print("\n")

print("Count of 1 in tuple:", tuple.count(1)) #count the number of times a specified value occurs in a tuple
print("index of 1 in tuple:", tuple.index(1)) #search the tuple for a specified value and return the position of where    

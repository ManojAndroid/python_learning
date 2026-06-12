

list=[1,2,3,4,5]

#iterate list using for loop

for i in list:
    print(i,end=" ")  # Output: 1 2 3 4 5

 # add in list
list.append(6)  # Output: [1, 2, 3, 4, 5, 6]
print("\nList after append:", list)   


list.insert(0,10)  # Output: [10, 1, 2, 3, 4, 5, 6]
print("List after insert:", list)

#empty list
list2=[]

for i in range(1,11):
    list2.append(i)


print("List after appending", list2)


list2.remove(5)  # Output: [1, 2, 3, 4, 6, 7, 8, 9, 10]
print("List after removing 5:", list2)

list2.pop()  # Output: [1, 2, 3, 4, 6, 7, 8, 9] pops last element
print("List after popping last element:", list2)

list2.clear

print("List after removing", list2)

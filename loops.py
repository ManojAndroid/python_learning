
#for i in range(5):
 #   print(i)

#range(5)  endt at 5
#range(0, 6)  start at 0 and end at 4   n+1
#range(1,21,1)  start at 1, end at 20, and step by 1

for i in range(0, 11):
    print(i)

#string range
#a="student"
#for i in a:
 #   print(i)

# index value 

a="student"
for i in range(len(a)):
    print(a[i],end="")


    n=10
    print("while loop")

    while n>0:
        print(n)
        n=n-1

    print("list loop")
    List=[5,2,3,4,5]
    List.insert(2,10)  # insert 10 at index 2
    List.sort(reverse=True)  # sort the list in descending order
    for i in List:
        print(i)      




# class is used to create user-defined data structures. A class is a blueprint for creating objects.
#  An object has properties and methods(functions) associated with it.
#  Almost everything in Python is an object, with its properties and methods.

class test:
    a = 10

test=test();
print(test.a)



class test2:
    
    def __init__(self,name):
        self.a = 10
        self.name = name

    def display(self):
        print("This is a method of the class test2")   

    def add(self,x,y):
        return x+y     

xtest2=test2("Alice");
print("Ttest2")
print(xtest2.a)        
print(xtest2.name)
xtest2.display()
print(xtest2.add(5, 3))

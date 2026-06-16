
class parent:
    def __init__(self):
        print("This is parent class")

    def parent_method(self):
        print("This is parent method")


 
 
class Child(parent):
     def __init__(self,name):
         super().__init__()
         self.name=name
           


child= Child("manoj")
print(child.name)
child.parent_method()

def greet(name):
    print(f"Hello, {name}!")

    
greet("manoj")  # This will print "Hello, manoj!"

print("position arguments example:")

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

sum=add(2, 3)  # This will return 5

print(sum)  # Output: 5


print("default arguments example:")

def addition(a,b=5):
    """Returns the sum of a and b, with a default value for b."""
    return a + b
result=addition(10)  # This will return 15, since b defaults to 5
print(result)  # Output: 15

print("keyword arguments example:")
def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

product = multiply(y=4, x=3)  # This will return 12, using keyword arguments
print(product)  # Output: 12
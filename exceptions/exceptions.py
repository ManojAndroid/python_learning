# exceptions are defined here

class InvalidInputError(Exception):
    """Exception raised for invalid input."""
    pass

#pass can be used as a placeholder for future code or to indicate that a block of code is intentionally left empty.

class NotFoundError(Exception):
    """Exception raised when a resource is not found."""
    pass

# exception operations can be defined here

try:
    # some code that may raise an exception
    raise InvalidInputError("This is an invalid input error.")
except Exception as e:
    print(f"Caught an exception: {e}")

# exception relatd all keyword and operations can be defined here

# add finally block if needed
try:
    # some code that may raise an exception
    raise NotFoundError("This resource was not found.")
except NotFoundError as e:
    print(f"Caught an exception: {e}")
finally:    
    print("This will always execute, regardless of whether an exception was raised or not.")
    
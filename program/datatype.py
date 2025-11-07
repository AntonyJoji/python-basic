# Data Types in Python
# 1. Numeric Types
#    - int: Integer values (e.g., 5, -3, 0)
#    - float: Floating-point values (e.g., 3.14, -0.001)
#    - complex: Complex numbers (e.g., 2 + 3j)      
# 2. Sequence Types
#    - list: Ordered, mutable collection (e.g., [1, 2, 3])
#    - tuple: Ordered, immutable collection (e.g., (1, 2, 3))
#    - range: Immutable sequence of numbers (e.g., range(0, 10))
# 3. Text Type
#    - str: Immutable sequence of Unicode characters (e.g., "Hello, World!")            
# 4. Set Types
#    - set: Unordered collection of unique elements (e.g., {1, 2, 3})
#    - frozenset: Immutable version of set (e.g., frozenset([1, 2, 3]))
# 5. Mapping Type
#    - dict: Collection of key-value pairs (e.g., {"name": "Alice", "age": 30}) 
# 6. Boolean Type
#    - bool: Represents True or False values
# 7. Binary Types
#    - bytes: Immutable sequence of bytes (e.g., b"Hello")
#    - bytearray: Mutable sequence of bytes (e.g., bytearray(b"Hello"))
#    - memoryview: Memory view object (e.g., memoryview(b"Hello")))
# 8. None Type
#    - NoneType: Represents the absence of a value (e.g., None)
# Note: Python is dynamically typed, so you don't need to declare the type of a variable explicitly.    
# Example Usage:
#x = 10               # int
#y = 3.14             # float
#z = 2 + 3j           # complex
#my_list = [1, 2, 3]  # list
#my_tuple = (1, 2, 3) # tuple
#my_range = range(0, 10) # range
#my_str = "Hello, World!" # str
#my_set = {1, 2, 3}   # set
#my_frozenset = frozenset([1, 2, 3]) # frozenset
#my_dict = {"name": "Alice", "age": 30} # dict
#is_active = True     # bool
#my_bytes = b"Hello"  # bytes
#my_bytearray = bytearray(b"Hello")  # bytearray
#my_memoryview = memoryview(b"Hello") # memoryview
#my_none = None       # NoneType
# ###################################

#numercial types
'''a=5
print(a)
print(type(a))  

# float
b=3.14
print(b)
print(type(b))

# complex
c=2 + 3j
print(c)
print(type(c))
print(c.real)  # Real part
print(c.imag)  # Imaginary part
print(c.conjugate())  # Conjugate'''

# ###################################

#sequence types
# list
'''my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

# tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))

# range
my_range = range(0, 10)
print(my_range)
print(type(my_range))'''

# ###################################


#mapping type
# dict
'''my_dict = {"name": "Alice", "age": 30}
print(my_dict)
print(type(my_dict))
print(my_dict["name"])  # Accessing value by key'''

# ###################################

#boolean type
# bool
'''val = True
print(val)
print(type(val))
is_logged_in = False
print(is_logged_in)
print(type(is_logged_in))'''

#examples
'''val=10>5
print(val)

val=10==5
print(val)'''

# ###################################

#set types
# set   
'''my_set = {1, 2, 3, 4, 5}
my_set=frozenset(my_set)
print(my_set)
print(type(my_set))'''

########################################


#sequence types
# str
'''my_str = "Hello, World! , 12e3111114"
print(my_str)
print(type(my_str))'''


# ###################################

#list
'''my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))'''

# ###################################

#tuple
'''my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))'''

# ###################################


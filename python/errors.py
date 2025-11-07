# arithamatic errors.py

#SyntaxError

#print("Hello"   # Missing closing parenthesis
#NameError
#print(x)  # x is not defined
#TypeError
#print("Hello" + 5)  # Cannot concatenate str and int
# ###################################

#variables.py

#1. What is a Variable?
#A variable is a named location in memory used to store data.
#2. Variable Naming Rules
#✅ Allowed:
#   - Letters (a-z, A-Z)
#   - Digits (0-9)
#   - Underscore (_)
#❌ Not allowed:
#   - Cannot start with a digit.
#   - No special symbols (@, $, %).
#   - Cannot use Python keywords (if, for, while, etc.).
#3. Best Practices
#   - Use meaningful names (e.g., total_price, is_active).
#   - Follow a consistent naming convention (e.g., snake_case).
# a=10
# b=10
# print(id(a))
# print(id(b)) # same id because of interning, it points to same memory location

# #######################################################

###### identifiers.py###############

#1. What is an Identifier?

#An identifier is a name used to identify a variable, function, class, module, or other object in Python.

#2. Naming Rules

#✅ Allowed:

    #Letters (a-z, A-Z)

    #Digits (0-9)

    #   Underscore (_)

#❌ Not allowed:

#Cannot start with a digit.

#No special symbols (@, $, %).

#Cannot use Python keywords (if, for, while, etc.).

#3. Best Practices

#Use meaningful names (e.g., total_price, is_active).

#Follow a consistent naming convention (e.g., snake_case).

#Avoid single-character names except for counters or iterators (e.g., i, j).
#Avoid using names that are too similar to built-in names (e.g., list, str).
# #######################################################
#4. Examples
# Valid identifiers
# my_variable = 10
# _private_var = "Hello"        
# var123 = 45.67
# Invalid identifiers
# 2nd_var = 100  # ❌ starts with a number
# for = "loop"   # ❌ keyword
# my-variable = 5 # ❌ hyphen not allowed
# $dollar = 50   # ❌ special character
# #######################################################

#5. Common Mistakes
#Using keywords as identifiers.
#Starting identifiers with digits.
#Using special characters in identifiers.
#Using spaces in identifiers.
#Using inconsistent naming conventions.
# #######################################################
#6. Summary
#Identifiers are names used to identify variables and other objects in Python.
#They must follow specific naming rules and best practices to ensure code readability and maintainability.

#Proper use of identifiers is crucial for writing clean and efficient code.
# #######################################################
#7. Practice
#Create variables using valid identifiers.
#Avoid using invalid identifiers and observe the errors.
#Review and refactor existing code to improve identifier names.
# #######################################################
#8. Additional Resources    
#Python's official documentation on identifiers: https://docs.python.org/3/reference/lexical_analysis.html#identifiers
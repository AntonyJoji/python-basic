## first class function

# def greet():
#     return "hello antony"

# print(greet())

# ## exmaple of first calss function
# res = greet ## assigning function to variable
# print(res())## calling function using variable


# ## passing fuction as argument to another function

# def sqr(x):
#     return x*x
# def cube(x):
#     return x*x*x

# print(cube(sqr(2))) ## calling function inside another function

# def sqr(x):
#     return x*x

# def apply(func,value):## function as argument
#     return func(value)

# print(apply(sqr,5)) ## passing function as argument to another function


# def outer():
#     def inner():
#         return "hello antony"
#     return inner() ## returning function call also its example for higher order function

# func = outer() ## calling outer function
# print(func)## printing returned value from outer function


## storing function as collection

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b


# val = [add,sub,mul]## storing functions in list

# for func in val:
#     print(func(10,5))## calling each function from list



######################################################

# def applay(func,x,y):
#     return func(x,y)
# print(applay (lambda a,b:a+b,5,3))  ##higher order function with lambda function

##########################################################
### closure fuction 
## function defined inside another function and returned from that function is called closure function


# def outer ():
#     msg ='hello'
#     def inner(): ## inner function ie. inner function can access variable of outer function after outer function has finished its execution
#         print(msg)
#     return inner

# val = outer() ## returning function object
# print (val.__name__) ## printing function name
# val() ## printing function object


# def logger(x):
#     def log_msg():
#         print("msg:",x)
#     return log_msg

# val =logger("hello antony")## returning function object
# print(val.__name__)## printing function name
# val()## calling logger function


# def html_tag(tag):
#     def wrap_msg(msg):
#         print(f"<{tag}>{msg}</{tag}>")
#     return wrap_msg

# res= html_tag("h1") ## returning function object
# res("first line") ## calling returned function


# def outer():
#     count =0
#     def increment():
#         nonlocal count ## to modify variable of outer function so we use nonlocal keyword
#         count+=1
#         return count
#     return increment
# val = outer()
# print(val())


# def bank_account (initial_balance):
#     balance = initial_balance

#     def transation(amt):
#         nonlocal balance
#         if balance+amt>=0:
#             balance += amt
#             return  f"balance: {balance}"
#         else:
#             return "insufficient balance"
#     return transation
    
# acc = bank_account(1000)
# print(acc(500))
# print(acc(-500))
# print(acc(-2000))
    


# def decorator_function(original_function):
#     def warapper_function():
#         print(f"wrapper executed befor the {original_function.__name__}")
#         return original_function()
#     return warapper_function

# def display():
#     print("this is display function")


# wrapped = decorator_function(display) ## passing function to decorator function
# wrapped() ## calling wrapper function

# def decorator_function(original_function):
#     def warapper_function():
#         print(f"wrapper executed befor the {original_function.__name__}")
#         return original_function()
#     return warapper_function

# @decorator_function ## syntax to apply decorator
# def display():
#     print("this is display function")

# display()



# def decorator_function(original_function):
#     def warapper_function(name,age):
#         print(f"wrapper executed befor the {original_function.__name__}")
#         return original_function(name,age)
#     return warapper_function

# @decorator_function ## syntax to apply decorator
# def display(name,age):
#     print(f"this is display function with arguments {name}{age}")

# display('antony',24)


def decorator_function(original_function):
    def warapper_function(*a):
        print(f"wrapper executed befor the {original_function.__name__}")
        return original_function(*a)
    return warapper_function

@decorator_function ## syntax to apply decorator
def display(name,age):
    print(f"this is display function with arguments {name}{age}")

display('antony',24)

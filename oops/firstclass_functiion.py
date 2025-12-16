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


# def decorator_function(original_function):
#     def warapper_function(*a):
#         print(f"wrapper executed befor the {original_function.__name__}")
#         return original_function(*a)
#     return warapper_function

# @decorator_function ## syntax to apply decorator
# def display(name,age):
#     print(f"this is display function with arguments {name}{age}")

# display('antony',24)

  ################################3 class as decorator###########################
# class decorator_class:
#     def __init__(self,org_function): # constructor
#         self.org_function =org_function# constructor to take original function as argument
#     def __call__(self, *args, **kwargs):## need to conver to the callable object
#         print(f"warapper execution before {self.org_function.__name__}")# printing original function name
#         return self.org_function(*args,**kwargs)## calling original function




# @decorator_class
# def display():
#     print("this is display function")
# display()## decordted class calling
# @decorator_class
# def display_info():
#     print("this is display function_info function! with arguments {name} {age}")
# display_info("ram",24)## decordted class calling

# import time 
# def calc_timesqr(numbers):
#     start_time=time.time()
#     res =[]
#     for num in numbers:
#         res.append(num*num)
#     end = time.time()
#     print (f'{calc_timesqr.__name__}:{(end-start_time)*1000}mille sec')

#     return res

# array = range(1,10001)
# sqr =calc_timesqr(array)
# # print(sqr)


# import time 
# def find_time (func):
#     def warpper(*args,**kwardgs):
#         start =time.time()
#         calctime=func(*args,**kwardgs)
#         end =time.time()
#         print(f'{calc_timesqr.__name__}:{(end-start)*1000}mille sec')
#         return calctime
#     return warpper

# @find_time
# def calc_timesqr(numbers):
#     res =[]
#     for num in numbers:
#         res.append(num*num)

#     return res

# def calc_timecube(number):
#     res =[]
#     for num in number:
#         res.append(num**3)
#     return res



# array = range(1,10001)
# sqr =calc_timesqr(array)
# cube =calc_timecube(array)


# def decorator_with_arg(msg):
#     def actual_decorator(func):
#         def warpper(*args):
#             print(f"{msg}-before calling{func.__name__}")
#             result =func(*args)
#             print(result)
#             print(f"{msg}-after calling {func.__name__}")
#             return result
#         return warpper
    
#     return actual_decorator
    
# @decorator_with_arg("coustom log message")
# def say_hello(name):
#     return f"Hello {name}"

# res=say_hello("anto")



# def uppercase_decorator(func):
#     def wrapper1(*args):
#         result =func(*args)
#         return result.upper()
#     return wrapper1

# def exclamation_decorator(func):
#     def wrapper2(*args):
#         result= func(*args)
#         return result + '!'
    
#     return wrapper2

# class greeting:
#     def __init__(self,name):
#         self.name =name

#     @exclamation_decorator
#     @uppercase_decorator # wrapper 1
#     def say_hello(self):## wrapper 2
#         return f"hello {self.name}"
    
# greet =greeting("anto")
# print(greet.say_hello())



class sample:
    value =" hi"
    def getval(self):
        value ="hello"
        print(f'the value is:{self.value}')

new = sample()
new.getval()
newone =sample()
newone.getval()
# del newone ## to delete the instance 
sample.value="hola"
print(sample.value)
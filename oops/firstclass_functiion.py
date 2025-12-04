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


def html_tag(tag):
    def wrap_msg(msg):
        print(f"<{tag}>{msg}</{tag}>")
    return wrap_msg

res= html_tag("h1") ## returning function object
res("first line") ## calling returned function
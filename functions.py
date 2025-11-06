# def cal():
#     print('hello')

# cal()
# print("done")



# def addvals():
#     a=10
#     b=21
#     res=a+b
#     print(res)

# addvals()
# addvals()

# def addvals(a,b):
#     res=a+b
#     print(res)

# addvals(20,30)
# addvals(1,3)
# addvals(30,70)   

# def squr_ls(val):
#     ls=[]
#     for i in range(1,val+1):
#         ls.append(i*i)
#     print (ls)

    

# squr_ls(100)

# def squr_ls(val):
#     ls=[]
#     for i in range(1,val+1):
#         ls.append(i*i)
#     return ls

    

# ls =squr_ls(10)
# ls = squr_ls(100)

# def find_even(a):
#     res=[]
#     for i in a:
#         if i%2==0:
#             res.append(i)
#     return res


# result = find_even(ls)
# print (result)

# def avge():
#     a=int(input("enter the number:"))
#     numbers=[]
    
#     for i in range(a):
#         num = float(input("Enter a number: "))
#         numbers.append(num)

#     average = sum(numbers)/len(numbers)
#     print (average)
# avge()
##########or############

# def avrg(val):
#     ls=[]
#     for i in range(val):
#         num=int(input("enter the number"))
#         ls.append(num)
#     return sum(ls)/len(ls)

# val= int (input("enter hte count:-"))
# result=avrg(val)
# print (result)



# def avrg():
#     val = int (input("enter the count:-"))
#     sum=0
#     for i in range(val):
#         sum+=int(input("enter the value;-"))
#     return sum/val
##############################################################
# result =avrg()
# print (result)
    

# name1 = "Devin"
# name2 = "Abin"

# def callme():
#     print(f"Hi {name1}, and this is {name2}.")

# def call(val):
#     Name = "Dainty"
#     print(f"Hi {Name}, he is {val}.")

# call("Awesome")
# callme()


    
# def samp(a,b,c):# possitional argument passing
#     print(a)
#     print(b)
#     print(c)

# samp(1,2,3)

# def samp(a,b=0,c=0):# #default argument passing
#     print(a)
#     print(b)
#     print(c)

# samp(1,2,3)

# def samp(a,b):#keyword argument passing
#     print(a-b)

# samp(b=4,a=2)

# def samp(*a):#arbitary argument
#     print(a)
#     for i in a:
#         print(i)

# samp(1,2,3,4)

# def samp(**a):#keyword arbitary argument
#     print(a)
#     for i in a.values():
#         print(i)

# samp(a=1,b=2,c=3)
# samp()

####################################
#factorial of a number

# def factorial(n):
#     if n < 0:
#         return "nope"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# num = int(input("enter the number:"))
# res = factorial(num)
# print(res)

##write a function second_largest (nums) that return the second largest element in a list



# def second_largest(nums):
#     unique_nums = list(set(nums))      # Remove duplicates
#     unique_nums.sort(reverse=True)     # Sort in descending order
#     return unique_nums[1]              # Return second largest

# # Get list input from user
# n = int(input("Enter how many numbers: "))
# nums = []

# for i in range(n):
#     val = int(input(f"Enter number {i+1}: "))
#     nums.append(val)

# print("List:", nums)
# print("Second largest number:", second_largest(nums))

#####################################################################
#write a function count_frequency(ist)that return a dictionary of each element

#ls =['a','b','a','c','b','a']

# def coun_freq(lst):
#     freq={}
#     for i in lst:
#         freq[i]=freq.get(i,0)+1
#     return freq


# ls = ['a', 'b', 'a', 'c', 'b', 'a']
# print(coun_freq(ls))

# def count_frequency(lst):
#     freq = {}  # empty dictionary to store counts
#     for item in lst:
#         if item in freq:
#             freq[item] += 1   # increase count if already present
#         else:
#             freq[item] = 1    # set to 1 if new item
#     return freq

# ls = ['a', 'b', 'a', 'c', 'b', 'd']
# print(count_frequency(ls))


###################################################
# # lambda function
# #  syntax: lambda arguments: expression 
# #its an anonymous function it dosent have name,it means we can define and call it in single line

# def add_val(a,b,c):
#     res =a+b+c 
#     return res
# print(add_val(1,2,3))

# print((lambda a,b,c:a+b+c)(10,20,30))

# res = lambda a,b,c:a+b+c
# print(res(100,200,300))


# res = lambda a,b:a if a>b else b
# print(res(100,200))



# #if we need to sort with length
# ls =['#','abcd','abc','@abc'] # list of strings
# ls.sort(key=lambda x:len(x)) # sort based on length of each string by using lambda function as key
# print(ls)

# def func(v=2):
#     c =v*2
#     return c
# x=2
# high=lambda x,func:x+func
# print(high(3,func()))

# grade =lambda val :'A' if val>=990 else 'B' if val>=75 else 'C' if val>=50 else 'Fail'
# print(grade(95))
# print(grade(75))
# print(grade(84))
# print(grade(50))
# print(grade(30))

# data =[(1,5),(2,1),(3,7),(4,3)]
# data.sort(key=lambda x:x[1])
# print (data)


# data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}, {'name': 'Bob', 'age': 30}]
# data.sort(key=lambda x:x['age'])
# print(data)

# data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}, {'name': 'Bob', 'age': 30}]
# str=sorted(data,key=lambda x:x['age'])
# print(data)
# print(str)

#function composition


# def f(x):
#     return x+2

# def g(x):
#     return x*3

# def compose(f,g):
#     return lambda x:f(g(x))

# res =compose (f,g)
# print(res(5))

# f= lambda x:x+2
# g=lambda x:x*3
# compse =lambda f,g:lambda x:f(g(x))
# res =compose(f,g)
# print(res(5))



# val="hello python"

# def rm_spaces(data):
#     return data.strip()

# def to_lower(data):
#     return data.lower()

# def compose(a,b,val):
#     return a(b(val))

# print(compose(rm_spaces,to_lower,val))


# nums =[1,2,3,4,5,6,7,8,9,10]

# def even(data):
#     return [i for i in data if i%2==0]

# def sqr(data):
#     return [i*i for i in data]

# def compose(a,b,data):
#     return a(b(data))

# print (compose(sqr,even,nums))


#################################################
# #function recursion ,a function calling itself

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     elif n<0:
#         return "no fact"
#     else:
#         return n * factorial(n-1)

# num = int(input("enter the number:"))
# res = factorial(num)
# if res == "no fact":
#     print(f"there is no fact {num}")
# else:

#   print("Factorial:", res)
#########################################################
##sum of n natural number########

# def sum_num(n):
#     if n==0:
#         return n
#     return n+sum_num(n-1)

# print (sum_num(5))

#########count the digit of a number###############
# val=4356
# def count_digit(num):
#     if num==0:
#         return 0
#     return 1+count_digit(num//10)
# print(count_digit(val))

#ls =[1,2,3,4,5]

# def list_sum(ls):
#     if len(ls)==0:
#         return 0
#     else:
#         return ls[0]+list_sum(ls[1:])
    
# ls=[1,2,3,4,5]
# print (list_sum(ls))
###################################################
#### find the work flow of the program :)
# ls=[1,[2,3],4,[5,6]]

# def ls_sum(data):
#     total =0
#     for val in data:
#         if type (val)==type([]):
#             total=total+ls_sum(val)
#         else:
#             total= total+val
#     return total

# print (ls_sum(ls))

#################Enumerate_function################################
##Enumerate_function is a built-in function in Python that adds a counter to an iterable and returns it as an enumerate object. 
##This is particularly useful when you need both the index and the value of items in a loop.
# to print index and value
# ls =['red','black','blue']
# vals = ['red','black','blue']
# for i in range (len(vals)):
#      print(i,vals[i])

# # or

# vals = ['red','black','blue']

# for i in enumerate(vals):
#     print(i)

##########map,reduce,filter#############
## map function is used to apply a function to all the items in an input list (or any iterable) and return an iterator (map object) of the results.

# def sqr(a):
#     return a*a

# ls= [1,2,3,4]
# # print(sqr(ls))
# print(map(sqr,ls)) #map object
# print(list(map(sqr,ls))) # convert map object to list
# ## or
# print (list(map(lambda x:x*x,ls))) # using lambda function


### filter function is used to filter items from an input list (or any iterable) based on a specified condition and return an iterator (filter object) containing only the items that satisfy the condition.

# nums =[1,2,3,4,5,6,7,8,9,10]
# print(filter(lambda x:x%2==0,nums)) #filter object
# print(list(filter(lambda x:x%2==0,nums))) # convert filter object to list if the condition is true

#### reduce function is used to apply a binary function (a function that takes two arguments) cumulatively to the items of an input list (or any iterable) from left to right,
#### or reducing the iterable to a single value.

# from functools import reduce
# ls=[1,2,3,4,5]
# print(reduce(lambda x,y:x+y,ls)) # sum of all elements
# print(reduce(lambda x,y:x*y,ls)) # multiplication of all elements
##########################################

# val =['red','black','blue'] # convert all to uppercase
# ls=[]
# for i in val:
#     ls.append(i.upper())
# print(ls)

# #or
# print(list(map(lambda x:x.upper(),val)))

################################################

# val =['red','black','blue']# length of each string
# ls=[]
# for i in val:
#     ls.append(len(i))
# print(ls)

# ##or
# print(list(map(lambda x:len(x),val)))


# val =[10,30,20]# store in string
# ls =[]
# for i in val:
#     ls.append(str(i))
# print(ls)

# ##or
# print(list(map(str,val)))


# nums =[4,5,6,7]#  multiply by its index possition
# ls =[]
# for i in range(len(nums)):
#     ls.append(nums[i]*i)
# print(ls)

# ##or
# print(list(map(lambda x:x[0]*x[1],enumerate(nums))))


# ls =[(50,60,50),(35,45,30),(65,85,25)]# to find the total score of each tuple
# total_scores =[]
# for scores in ls:
#     total=0
#     for score in scores:
#         total+=score
#         total_scores.append(total)
# print(total_scores)


##or
# print(list(map(lambda x:x[0]+x[1]+x[2],ls)))
# ##or
# print(list(map(lambda x:sum(x),ls)))


# ls = ['antony@gmail.com','rem@yahoo.com','re@python.org']# to extract the domain names from the email addresses
# domain_names=[]
# for email in ls:
#     domain_names.append(email.split('@')[1])
# print(domain_names)

# ##or
# print(list(map(lambda x:x.split('@')[1],ls)))

####################################################

# data =['10','20','abc','30','xyz'] #conver this list of strings to integers,ignore the nonn numeric values to non numeric vallues

# def find_int(x):
#     if x.isdigit():
#         return int(x)
#     else:
#         return None
# print(list(map(find_int,data)))

#################################################

# ls =['01/02/2020','15/03/2021','31/12/2019'] # yyyy-mm-dd format

# def convert_data(date_str):
#     day,month,year =date_str.split('/')
#     return print(year+'-'+month+'-'+day)
# print(list(map(convert_data,ls)))

# ##or

# print(list(map(lambda x:'/'.join(x.split('/')[::-1]),ls)))



# words =['data','java','python','AI','ML'] #  those with length greater than 3 characters print
# print(list(filter(lambda x:len(x)>4,words)))



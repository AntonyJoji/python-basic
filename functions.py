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

def squr_ls(val):
    ls=[]
    for i in range(1,val+1):
        ls.append(i*i)
    return ls

    

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




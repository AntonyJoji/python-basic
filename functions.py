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


##########################################################
#####  MODULES AND PACKAGES  ##########
###########################################################

# import time as t
# from time import time
# from time import *
# # avoid wildcard imports and redundant imports
# # print(dir(t))
# # print(help(t))

# # print(t.time())
# # print(t.localtime(t.time()))


# tp = (1956, 10, 5, 0, 0, 0, 0, 0, 0)  # time tuple
# timestamp = t.mktime(tp)
# print(timestamp)
# print(t.localtime(timestamp))

# t.sleep(5)
# print("hello in 5 seconds")


# import timeit
# # measure creating a list comprehension multiple times
# print(timeit.timeit('[i*i for i in range(1,11)]', number=10000))

######################################################################

# import calendar as cal
# print(dir(cal))
# print(cal.calendar(2023))
# print(cal.isleap(2028))
# print(f"leap days: b/w 1995 to 2025:-{cal.leapdays(1995,2025)}")

# print (cal.month(2025,2))
# print(cal.month(2025,11,3,2))

# print(cal.weekday(1880,11,5))

#########################################################################

# from asyncio import sleep
import datetime as dt

# print(dt.date(2024,5,12))

# d=dt.date(2024,5,12)
# print(d.today())
# print(d.month)
# print(dt.date.today())


# d= dt.date.today()
# print(d.weekday())
# print(d.isoweekday())


# now=dt.datetime.now()
# print(now)
# date = now.strftime("%d-%m-%y  %H:%M:%S")


# d= dt.date.today()
# td =dt.timedelta(days=4)
# print(d+td)
# print(d-td)


#####################################################################

########## Random #########################################
import random as rd
# print (rd.random())
# val=rd.uniform(1,10)
# print(val)

# val = rd.randint (1,100)
# print(val)


# val =rd.randrange(1,100,5)# step size 5 it will pick only those numbers which are multiple of 5
# print (val)

# ls = ['apple','banana','mango','grape','orange']
# val =rd.choice(ls)
# print (val)

# ls = ['apple','banana','mango','grape','orange','kiwi','pineapple','peach']
# val =rd.choices(ls,k=3)
# print (val)


# ls =['red','blue','black']
# val =rd.choices(ls,weights=[10,30,60],k=5)
# print (val)


# ls = ['hello','hola','hallo','ciao','salut','howdy','namaste','salaam','shalom']
# val =rd.choice(ls)
# print (val)

# val = list(range(1,21))
# print (val)
# rd.shuffle(val)
# print (val)

## difference between sample and choices :- sample is without replacement and choices is with replacement or sample can not pick same element again but choices can pick same element again.


# ls =['red','blue','black','green','yellow','white','pink','purple']

# val =rd.sample(ls,k=1)
# print(val)
######################################################################################################################


# firstname = ["devin", "dainty", "abin", "jessica", "ashna", "afitha"]
# lastname = ["mathew", "mathew", "eldhose", "joseph", "hasif", "jabbar"]
# streetname = ["high", "lon", "lose", "hola", "warks", "rody"]
# states = ["AL", "KL", "ML", "CP", "EK", "DL"]
# fakecities = ["logsow", "florida", "poland", "germany", "prague", "austria"]

# for i in range(10):
#     first =rd.choice(firstname)
#     last =rd.choice(lastname)
#     phone= f"{rd.randint(100,999)}--555---{rd.randint(100,999)}"

#     street =rd.choice(streetname)
#     state=rd.choice(states)
#     city=rd.choice(fakecities)
#     zipcode =rd.randint(10000,99999)
#     address =f"{zipcode}{street} {city} {state}"
#     mail = first+"." + last + "@fakeemail.com"
#     print(f"Name: {first} {last}\nPhone: {phone}\nAddress: {address}\nEmail: {mail}\n")



##############################################################################################

# from time import sleep
# lottery_tickets=[]
# print("creating tickets...")
# for i in range(100):
#     lottery_tickets.append(rd.randrange(100000,999999))
# v = rd.sample(lottery_tickets,k=1)
# print("finding winner ticket.... please wait")
# sleep(6)
# print(f"winner ticket is :{v}")

#######################################################################################

# val =isinstance(5, list)
# print (val)

# val =isinstance(5,int)
# print(val)

# val =isinstance(5,(float,int,set,str,list))
# print(val)

###############################################################################################
 ## Any
 ## All



# a= [False,True,True,True]
# print(any(a))  # true if any one element is true
# print(all(a))  # true if all elements are true


# a=['','ab','abc']
# print (any(a))

# a= ['','abc','abcd']
# print(all(a))


# a=[0,1,2,3,4,5]
# print(any(a)) # true because non zero numbers are considered as true in boolean context
# print(all(a)) # false because 0 is considered as false in boolean context


###################################################################################################

####  ABS  #########################

# a = -11
# print(abs(a))  # absolute value

# b= -56.67
# print(abs(b))

###### ROUND  ############################

# print(round(12.54))
# print(round(12.54678,2))

# print(min(3,4,5,5,-1,2))
# print(max(3,4,5,5,-1,2))

import math as m

# print (dir(m))

# print(m.pi)
# print(m.sqrt(16))
# print(m.sin(m.pi/2))


# print(m.floor(5.6))
# print(m.ceil(5.6))

# a,b =m.modf(100.12) # returns fractional and integer parts
# print(a)
# print(b)


from statistics import *

# print(mean([1,2,3,4,5,6,7,8,9]))# average
# print(median([1,2,3,4,5,6,7,8,9]))# middle value

# print(mode([1,2,3,4,3,2,3,8,9,4]))# most common value
# print(multimode([1,2,3,4,3,2,3,8,9,4]))# list of most common values
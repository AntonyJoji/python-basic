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


ls =['red','blue','black','green','yellow','white','pink','purple']
val =rd.sample(ls,k=1)
print(val)


### question 1 : print  jhon[smith]is a coder? // from formatstring.py :)
# first="john"
# last="smith"
# print("{0}[{1}] is a coder ".format(first,last))
# print(f"{first} [{last}] is a coder")


# question 2

# var1="it's sunday"
# var2='have a great day '

# it's a great day
#great sunday

# var1 = "it's sunday"
# var2 = "have a great day"
# part1 = var1.split() 
# part2 = var2.split() 
# print(part1[0], " ".join(part2[1:]))
# print(part2[2], part1[1])

# print(var1[:5] + " " + var2[7:])
# print(var2[5:] + " " + var1[5:])



# question 3

# text1 ="python programming"
# text2 ="is very powerfull"

# "# output: python is very powerfull"
# "powerful programming"
# #replace python with java
# extract only programming from text1
# join the first word of text1 and last word of text2  -> python powerfull
# is very powerful
# reverse only the first word of text1 -> nohtyp programming
# check if "very " exists in text2 -> True
# remove space and join both string -> pythonprogrammingisverypowerfull


# text1 = "python is very powerfull"
# text2 = "powerful programming"
# print(text1[:7] + text2)
# print(text1.replace("python", "java"))
# print(text2.split()[1])

# print(text1.split()[0], text2.split()[0])
# print(" ".join(text1.split()[1:]))
# print(text1.split()[0][::-1], text2.split()[1])
# print("very" in text2)
# print(text1.replace(" ", "") + text2.replace(" ", ""))
# result = text1.split()[0] + text2.split()[1] + "".join(text1.split()[1:])
# print(result)
## question 4
# val="the place is ekm"
# words=val.split()
# print(words)
# words[0]=words[0].capitalize()
# words[-1]=words[-1].capitalize()
# result=" ".join(words)
# print(result)


# question 4

# sub =['i','you']
# ver =['play','love']
# obj =['hokey','football']
# i play hocky
# i play foot ball
# i love hocky
# i love football
# you play hocky
# you play football
# you love hocky
# you love football

# sub = ['i', 'you']
# ver = ['play', 'love']
# obj = ['hockey', 'football']

# for s in sub:
#     for v in ver:
#         for o in obj:
#             print (s,v,o)

# question 5:
# with the give list [12,24,35,24,88,120,155,88,120,155]
# write a program to print this list after removing all
# duplicate value with orginal oder reserved

# list1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# new_list = []

# for i in list1:
#     if i not in new_list:# not in is used to check the item in the list
#         new_list.append(i)

# print(new_list)

# question 6
# write a program that accepts a sentence and calculate 
# the number of upper and lower case letter 
# suppose the following iinput is supplied to the program:
# "hello world"
# then the output should be 
# upper case 1
# lower case 9

# a=input("enter the string:")
# upper = 0
# lower = 0
# for b in a:
#     if b.isupper():
#         upper=upper+1
#     elif b.islower():
#      lower=lower+1
# print (upper)
# print (lower)     
# 

# val= input ("enter the string:")
# res ={"upper":0,"lower":0}  
# for i in val:
#     if i.isupper():
#         res['upper']+=1
#     elif i.islower():
#         res['lower']+=1     
# print (res)       
# 
# 
# ###########################
# 
# question7
# 
# 
# string = "a citizen of ekm fought and won the election"
# stop_words =["in","of","a","and","the" ]
# " citizen ekm fought won election"
# string = "a citizen of ekm fought and won the election"
# stop_word =["in","of","a","and","the"]
# wor=string.split()
# print (wor)
# ls=[]
# for i in wor:
#     if i not in stop_word:
#         ls.append(i)
# print (' '.join(ls) )

#question 8
#the number must be divisible 5
#write a program to display only those number from a list that satisfy the fllowing condition
# if the number is greater than 150 ,then skip it and move to the next number
#if the number is greater than 500 then stop  the loop

#number =[12,75,150,180,145,525,50]


# number =[12,75,150,180,145,525,50]

# for a in number:
#     if a>500:
#         break
#     elif a>150:
#         continue
#     elif a%5==0:
#         print(a)



########################

#['x','xx','xxx','xxxx']

#{1:'x',2:'xx',3:'xxx',4:'xxxx',5:'xxxxx'}

# my_list=[]
# for i in range(1,6):
#     my_list.append(i*'x')
# print (my_list)

###############################

# my_list={}
# for i in range (1,6):
#     my_list[i]=('x'*i)
# print(my_list)

#######################

#1
#1,2
#1,2,3
#1,2,3,4
#1,2,3,4,5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()    

#######################################
## to find the element fromo the list##########

# number=[4,2,7,1,8,3,6]
# n=int(input("enter the number to be find:"))
# for i in range(len(number)):
#     if number[i]==n:
#         print ("the number is fount:",n)
#         print ("the poposition:",i)
#         break
# else:
#     print("item not fount")
##################or############################

# number=[4,2,7,1,8,3,6]
# n=int(input("enter the number to be find:"))
# f=0
# for i in range(len(number)):
#     if number[i]==n:
#         print ("the number is fount:",n)
#         print ("the poposition:",i)
#         f=1
#         break
# if f==0:
#     print("item not fount")


    
   


 


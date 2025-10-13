# for i in "python":
#     print(i)


#list

# for i in[1,2,True,4.5,"hello"]:
#     print(i)

##########list examples########################

# list1=[10,20,30,40]
# for i in list1:
#     if i>=25:
#         print("value is greater than or equal to 25:",i)
#     else:
#         print("value is less than 25:",i)

######################################################

#while loops

# c=1
# while c<=5:
#     print(c)
#     c=c+1




######################################################
# s= "hello"
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1

######################################################
# for i in range(10):
#     print("hello")


# ls=[]
# for i in range(1,11):
#     ls.append(i+100)
# print(ls)



# ls=[]
# ls1=['python123','java123','c++123']
# for i in ls1:
#     ls.append(i.strip('123'))
# print(ls)

#user count add elements in list
# ls=[]
# a=int(input("enter a number:"))
# for i in range(a):
#     b=int(input("enter a number to add in list:"))
#     ls.append(b)
# print(ls)

# sum=0
# ls=[]
# a=int(input("enter a number:"))
# for i in range(a):
#     b=int(input("enter a number to add in list:"))
#     sum=sum+b
#     ls.append(b)
# print(ls)
# print("sum of all numbers:",sum)


# for i in range(1,4):
#     print('-->',i)
#     for j in range(3):
#         print('--->>>',j)


# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


ds={'a':10,'b':20,'c':30}
for i in ds:
    print(i,ds[i])
for i in ds.values():
    print(i)
for i in ds.keys():
    print(i)    
for i,j in ds.items():
    print(i,j)

# building data structures in python
# list
# tuple
# set
# dictionary

# ls = []#mutable, ordered collection of elements,
# print(type(ls)) # list is ordered collection of elements
# tuple = ()#immutable, ordered collection of elements,
# print(type(tuple))
# se = set() #{}#  unordered collection of unique elements,
# print(type(se)) # set is unordered collection of unique elements
# dict = {}# key value pairs,key should be unique, unordered collection of key value pairs
# print(type(dict)) # dictionary is collection of key value pairs


###################list##########################
# ls=[1,'hello',3.5,True,[10,20,30],(1,2,3),{1,2,3},{'name':'john','age':25}]#list can store different data types
# print(ls)
# print(ls[0])# first element
# print(ls[1])# second element
# print(ls[4])# fifth element
# print(ls[4][0])# first element of fifth element
# print(ls[-5])# fifth element from last
# print(ls[-1])# last element
# print(ls[1:4])# slicing
# print(ls[1:])# slicing from index 1 to end

#ls =[1,2,3,4,5,6,7,8,9,10]
# print(ls)
# print("odd elements using slicing")
# print(ls[::2])  # slicing #start:stop:step#2stepsize
# print("even elements using slicing")
# print(ls[1::2])
# print("reverse the list")
# print(ls[::-1])


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1.reverse() #inplace operation builtin function
# print(list1)
# print(len(list1))# length of the list
# print(min(list1))# minimum element in the list # must be of same data type
# print(max(list1))# maximum element in the list # must be of same data type
# print(sum(list1))# sum of all elements in the list # must be of same data type
# print(sorted(list1))# sorted list # must be of same data type


### to add elements to a list ##########
# ls=[]
# print(ls)
# ls.append(10)
# print(ls)
# ls.append(20)
# ls.append('hello')
# print(ls)
# ls.append([1,2,3])
# print(ls)# it will add the element at the end of the list

# a=input("enter a number :")
# ls.append(a)
# print(ls)

# ls.insert(2,'world')# it will insert the element at the given index
# print(ls)

# ls[4]='hi'
# print(ls) # it will replace the element at the given index


# a=[10,20,30,40,50,'hello']
# print(a)
# a.remove(30)# it will remove the first occurrence of the element
# print(a)
# a.pop()# it will remove the last element of the list
# print(a)
# ##or##
# del a[1]# it will remove the element at the given index1
# print(a)
# del a[1:2]# it will remove the elements from index 1 to 2
# print(a)
# a.clear()# it will remove all elements from the list
# print(a)


######sorting a list##########
# a=[10,5,3,7,2,1]
# print(a)
# a.sort()# it will sort the list in ascending order
# print(a)
# a.sort(reverse=True)# it will sort the list in descending order
# print(a)

# str1=["banana","apple","orange","kiwi","grape"]
# print(str1)
# str1.sort()# it will sort the list in ascending order
# print(str1)
###sort based on length of the string###
#
# print(str1)
# str1.sort(key=len)# it will sort the list based on the length of the string
# print(str1)

# a=["apple","banana"]
# b=[1,2,3]
# a.extend(b)# it will add the elements of list b to list a
# print(a)
# b.extend(a)# it will add the elements of list a to list b
# print(b)

##string to list##
# str1="hello world"
# print(str1)
# print(list(str1))# it will convert the string to list
# print(list((1,2,3,4)))# it will convert the tuple to list
# print(list({1,2,3,4}))# it will convert the set to list
# print(list({1:2,2:3,3:4,4:5}))# it will convert the dictionary to list (only keys)
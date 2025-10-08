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
# ls=[1,'hello',3.5,True,[10,20,30],(1,2,3),{1,2,3},{'name':'john','age':25}]#list can store different data types,mutable elements like list and set can be stored in list
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
#list1.reverse() #inplace operation builtin function
# print(list1)
#print(len(list1))# length of the list
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

# b=['python','java']
# a=b # both a and b are pointing to same memory location
# a.append(100)
# print(a)
# print(b)


## to create a copy of a list ##

# b=['python','java']
# a=b.copy() # it will create a copy of the list
# a.append(100)
# print(a)
# print(b)

### to count the occurrences of an element in a list ###
# a=['black','white','red','green','blue','red']
# print(a.count('black'))# it will count the number of occurrences of the element in the list
# print(a.count('red'))# it will count the number of occurrences of the element in the list


###########concatination of two lists##########
# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# print(c)

# a=['red','green','blue']
# b=['yellow','white','black']
# c=a+b
# print(c)


###index of an element in a list###
# a=['red','green','blue','yellow','white','black']
# print(a.index('blue'))# it will return the index of the first occurrence of the element
# print(a.index('white',2))# it will return the index of the first occurrence of the element from index 2
# print(a.index('black',2,4))# it will return the index of the first occurrence of the element from index 2 to 5



###################tuple##########################
# tup=(1,'hello',3.5,True,[10,20,30],{1,2,3},{'name':'john','age':25})#tuple can store different data types,immutable elements like list and set can be stored in tuple
# print(tup)
# print(tup[0])# first element
# print(tup[1])# second element

# print(min(tup))# it will give error because tuple contains different data types
# print(max(tup))# it will give error because tuple contains different data types
# print(len(tup))# length of the tuple
# print(sorted(tup))# it will give error because tuple contains different data types

# a=(10,20,30)
# val1,val2,val3=a#unpacking of tuple
# print(val1)
# print(val2)
# print(val3)

# a=(10,20,30)
# b=('hello','world')
# print(a+b)
# print(a*2)

# a=('black','white','red','green','blue','red')
# print(a.count('red'))# it will count the number of occurrences of the element in the tuple  
# print(a.index('blue'))# it will return the index of the first occurrence of the element
# print(a.index('blue',2))# it will return the index of the first occurrence of the element from index 2
# print(a.index('white',2,5))# it will return the index of the first occurrence of the element from index 2 to 5


###################set##########################
# se=set()#empty set, unordered collection of unique elements,immutable,duplicate elements are not allowed
# print(type(se))
# se={1,'hello',3.5,True,(1,2,3),frozenset({1,2,3}),('name','john'),('age',25)}#set can store different data types but not list and dictionary
# print(se)


##set operations##
# se={1,2,3,4,5}
# print(se)
# se.add(6)# it will add the element to the set
# se.add('hello')# it will add the element to the set
# print(se)

# se = frozenset(se)# it will convert the set to frozenset (immutable set)
# print(se)

# se={1,2,3,4,5}
# se.update([6,7,8,'hello',(1,2,3)])# update the set with the elements of the list
# print(se)

# se ={1,2,3,4,5}
# new = se.copy()# it will create a copy of the set
# print(id(se))
# print(id(new))


# se1={1,2,3}
# se2={3,4,5,'python','java'}
# print("union of two sets")
# new=se1.union(se2)# it will return the union of two sets
# print(new)
# print(se1|se2)# it will return the union of two sets

# print("intersection of two sets")
# new2=se1.intersection(se2)# it will return the intersection of two sets
# print(new2)

# print("difference of two sets")
# print(se1-se2)# it will return the difference of two sets
# print(se2.difference(se1))# it will return the difference of two sets
# print("symmetric difference of two sets")
# print(se1.symmetric_difference(se2))# it will return the symmetric difference of two sets

# print("to clear a set")
# print(se1.clear())# it will remove all elements from the set
# print(se1)

# print("subset and superset")
# se1={1,2,3}
# se2={1,2,3,4,5}
# print(se1.issubset(se2))# it will return True if se1 is subset of se2 else False
# print(se2.issuperset(se1))# it will return True if se2 is
# print(se2.issuperset(se1))# it will return True if se2 is superset of se1 else False

# se1={1,2,3,4,5}
# se1.remove(3)# it will remove the element from the set, if the element is not present it will raise an error
# print(se1)
# se1.pop()# it will remove a random element from the set
# print(se1)
# se1.discard(10)# it will remove the element from the set, if the element is not present it will not raise an error
# print(se1)


###################dictionary##########################

# d={} # empty dictionary, unordered collection of key value pairs,key should be unique,mutable
# print(type(d))# empty dictionary, unordered collection of key value pairs,key should be unique,mutable

# d={1:2,1.2:5,'a':'apple',(1,2):'hello',frozenset({1,2}):'world',True:200}#dictionary can store different data types but not list and set as key
# print(d[True])# accessing value by key'])

# val={'name':'john','age':25,'city':'new york','is_student':True,'marks':[90,80,85],'address':{'street':'5th avenue','zip':10001}}#nested dictionary
# print(val['address']['street'])# accessing value by key

# val={1:{1:2,2:{10:"hello",20:{1:100,2:200}}}}
# print(val[1][2][10])# accessing value by key
# print(val[1][2][20][1])# accessing value by key


# d={1:2,2:{1,2,3,4},3:'hello','a':100}
# print(d['a'])# accessing value by key
# print(d.get('b','key not found'))# it will return the value of the key if the key is present else it will return 'key not found'

# ls =[('developer','python'),('manager','java'),('analyst','javascript')]
# print(dict(ls))# it will convert the list of tuples to dictionary

# ls =['apple','banana','orange']
# ls2=['red','yellow','orange']
# new=zip(ls,ls2)
# print(dict(new))# it will convert the list of tuples to dictionary
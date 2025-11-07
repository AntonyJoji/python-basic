########   nested list   ###############################
# l=[[10,20],[30,40]]
# print(l)
# print(l[0])# first element
# print(l[1])# second element
# print(l[0][0])# first element of first list
# print(l[0][1])# second element of first list
# print(l[1][0])# first element of second list
# print(l[1][1])# second element of second list

############ replace###################
# l=[10,20,30,40,50]
# print(l)
# l[2]="hello"
# print(l)

###############insert##########################
# l=[10,20,30,40,50]
# print(l)
# l.insert(2,"hello")
# print(l)
# l.insert(0,"first")
# print(l)/
############example#######################
# a=[40,40,[10,20],[40,'hello']]#need to insert an element in b/w 10 and 20
# print(a)
# a[2].insert(1,65)
# print(a)
##################sort##########################
# l=["monkey","apple","cat","bear","elephant","dog"]
# l.sort()
# print(l)
#### example##########################
# l=[[35,75],[35,25]]
# l.sort()
# l[0].sort()
# print(l)

#################delete##########################

# l=[10,20,30,40,50]
# print(l)
# del l[0]
# print(l)

##################### pop##########################
# l=[10,20,30,40,50]
# print(l)
# l.pop()
# print(l)

#################append##########################

# l=[10,20,30,40,50]
# print(l)
# l.append("mango")
# print(l)

################reverse##########################
# l=["monkey","apple","cat","bear","elephant","dog"]
# l.reverse()
# print(l)

###############extend##########################
# l=['zebra','lion','giraffe']
# l1=['elephant','tiger']
# l.extend(l1)
# print(l)


####################question##########################
#Questions:
# Create a list of fruits. Perform the following operations:
# .a=["apple","banana"]
# 1.Replace "banana" with "grapes".
# 2.Insert "orange" between "apple" and "grapes".
# 3.Sort the list in descending order.
# 4.Delete the first item from the list.
# 5.Append "pineapple" to the end of the list.
# 6.Extend the list by adding another list of fruits ["strawberry", "mango"].


# a=["apple","banana"]
# print(a)
# print ("question 1")
# a[1]='grapes'
# print(a)
# print("question 2")
# a.insert(1,'orange')
# print(a)
# print("question 3")
# a.sort()
# print(a)
# a.reverse()
# print(a)
# print("question 4")
# del a[0]
# print(a) 
# print("question 5")
# a.append('pineapple')  
# print(a)
# print("question 6")
# a1=["strawberry","mango"]
# a.extend(a1)
# print(a)
# ls=[]
# for i in range (1,11):
#     ls.append(i*i)
# print(ls)

# print ([i*i for i in range (1,11)])


# ls=[]
# for i in range(1,11):
#     if 1%2==0:
#         ls.append(i)
# print(ls)

# print([i for i in range(1,11) if i%2==0])

# import math as m
# print(dir(m))
# print([m.sqrt(i) for i in range(1,11)]) 
# a=['devin','john','sonu']
# b=['lame','varun','last']
# print([(i,j) for i in a for j in b])

# ls=['even'if i%2==0 else 'odd' for i in range(1,11)]
# print (ls) /

# ls=[1,3,0,-2,5,-6,0,7]
# val=['positive' if i>0 else 'zero'if i==0 else 'negative' for i in ls]
# print(val)

# count=int(input("enter the count:"))
# ages=[]
# cat=[]
# for i in range(count):
#     age=int(input("enter the age:"))
#     ages.append(age)
#     if age<13:
#         cat.append("child")
#     elif age<20:
#         cat.append("teen")
#     elif age<45:
#         cat.append("adult")
#     else:
#         cat.append("Senior Citizen")
# print (ages)
# print(cat)

# ages=[('child',i)if i<13 else ('teen',i)if i<20 else('adult',i)if i<45 else ('senior',i) for i in ages]
# print(ages)
# val=[('child',i)if i<13 else ('teen',i)if i<20 else('adult',i)if i<45 else ('senior',i) for i in ages]
# print (val)

# val = [
#     ('Child', age) if age < 13 else 
#     ('Teen', age) if age < 20 else 
#     ('Adult', age) if age < 45 else 
#     ('Senior', age)
#     for age in [int(input("Enter age: ")) for _ in range(int(input("Enter number of people: ")))]
# ]

# print(val)

# ls=[[1,2],[3,4],[5,6],[7,8]]
# #o/p =[[1,3,5,7],[2,4,6,8]]
# print([[val[i] for val in ls]
#         for i in range(len(ls[0]))])


# ls=[[1,2],[3,4],[5,6],[7,8]]
# print ({j for i in ls for j in i})

#set

# val="antony joji"
# print({i for i in val})

# ls ={'even' if i%2==0 else 'odd'for i in range(1,11)}
# print (ls)


#dictonary

# ds={}
# for i in range(1,11):
#     ds[i]=i*i
# print (ds)


# ls={i:i*i for i in range(1,11)}
# print (ls)

# key=['devin','dainty','david']
# value=['python','cyber','analyst']
# ds={}
# for k,v in zip(key,value):
#     ds[k]=v
# print(ds)

# print ({k:v for k,v in zip(key,value)})

#genrator 

#in tuple the comprihention we need to fetch the element by using the loop or next method 
# #print([i for i in range(1,11) if i%2==0])  
# val=((i for i in range(1,11) if i%2==0))  
# # print (val)
# # for i in val:
# #     print (i)


# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))

# val = (
#     ('Child', age) if age < 13 else 
#     ('Teen', age) if age < 20 else 
#     ('Adult', age) if age < 45 else 
#     ('Senior', age)
#     for age in [int(input("Enter age: ")) for _ in range(int(input("Enter number of people: ")))]
# )
# print (val)
# for i in val:
#     print (i)
###or

# print(next(val))## if the loop the iteration is finish then it is dry if we call again it will produce an error

# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))
#############################################

# word =["apple","bananna","cherry"]
# cap=[]
# for a in word:
#     cap.append(a.upper())
# print (cap)
# word =["apple","bananna","cherry"]
# cap=[i.upper()for i in word]
# print (cap)


string= "comprehension"

# string = "comprehension"
# v = []
# for ch in string:         
#     if ch in "aeiou":      
#         v.append(ch)  
# print(v)
# val=([i for i in string if i in 'aeiou'])



# val=range(1,11)

# val=range(1,11)
# oddres=[]
# everes=[]
# for i in val:
#     if i%2!=0:
#         oddres.append(i*2)
#     else:
#         everes.append(i*3)
# print(oddres)
# print(everes)
# print ([1*2 if i%2==0 else i*3 for i in val])


# stri="python is amazing"
# words=stri.split()
# for i in words:
#     print(i)
#     print(len(i))

# a = [len(i) for i in stri.split()]
# print(a)


# #nums=[4,-1,2,-3,7,-5]

# nums = [4, -1, 2, -3, 7, -5]

# for i in range(len(nums)):
#     if nums[i] < 0:
#         nums[i] = 0

# print(nums)

# print([0 if i<0 else i for i in nums])


###################################

#find the uniqe vowel form the string

# string="programming"

string = "comprehension"
# vowels = "aeiou"
# unique_vowels = []
# for ch in string:
#     if ch in vowels and ch not in unique_vowels:
#         unique_vowels.append(ch)
# print(unique_vowels)

print ({i for i in string if i in "aeiou"})














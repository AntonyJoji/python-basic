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

ls=[[1,2],[3,4],[5,6],[7,8]]
#o/p =[[1,3,5,7],[2,4,6,8]]
print([[val[i] for val in ls]
        for i in range(len(ls[0]))])


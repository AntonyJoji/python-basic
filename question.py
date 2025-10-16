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






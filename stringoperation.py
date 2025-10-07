# val="hello my name is antony joji 123213424"
# print("lo" in val)

# val="antony joji"
# print (val)
# val[3]='a'



# upercase,lower,swapcase


# val="hi my name antony joji"
# print(val.upper())

# val="HELLO MY NAME IS ANTONY JOJI"
# print (val.lower())


# val ="HELLO my NAME IS  antony"
# print (val.swapcase())


# val="hi my name antony joji"
# print (val.islower())



# val="HELLO MY NAME IS ANTONY JOJI"
# print (val.isupper)


# val="hi my name antony joji"
# print (val.capitalize())#capitalize first word in sentence
# print (val.title())#capitalize every first word

# val="hi my name antony joji"
# print (val.count("a"))  #count the number of a in the string
# #print (val.strip())#remove the extra spaces in the string
# print (val.index("j",4))#find the index of n in the string
# print (val.find("j",4))#find the index of n in the string
# print (val.find("eq"))#find the index of n in the string if not found it will return -1
# print (val.find("e",17))#replace the string
# print (val.find('e',17,20))#replace the string
# print(val.find('e i',17,20))#replace the string


# val="himynameantonyjoji"# space not allowed if the space is there it will return false
# print (val.isalpha())

# val = "hi my name antony joji"
# print(val.replace("a", "@"))  # replace the string
# print(val.replace("a", "A", 1))  # replace the string only first


# val='1234567890'
# print(val.isdigit())#check the string is digit or not
# print(val.isnumeric())#check the string is numeric or not
# print(val.isdecimal())#check the string is decimal or not and it will return true only for 0-9


# vars='antony123'
# print(vars.isalnum())#check the string is alphanumeric or not

# val="hi my name antony joji"
# print(val.startswith("hi"))#check the string is start with hi or not

# print(val.endswith("h"))#check the string is end with joji or not
# print(val.endswith("a"))#check the string is end with antony or not


# val="hi my name-antony joji"
# print(val.split())#split the string and return as list
# print(val.split("-"))#split the string with - and return as list

# val="hi-my-name-antony joji"
# res=val.split('@')
# print(res)
# print('-'.join(res))#join the list with - and return as string

# val="     hi my name antony joji     "
# print(val)
# print(val.strip())#remove the extra spaces in the string
# print(val.lstrip())#remove the extra spaces in the left side of the string
# print(val.rstrip())#remove the extra spaces in the right side of the string


# val="<<<<---___hi my name antony joji ___--->>>"
# print(val)
# print(val.lstrip('-<>'))#remove the extra _<> in the string


# val="hi my name antony joji"
# print(val[12:])
# print(val[:12])
# print(val[3:12])
# print(val[3:12:2])#step count
# print(val[::2])#step count
# print(val[::-1])#reverse the string
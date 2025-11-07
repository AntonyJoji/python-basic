# ## format string####
# # string is immutable
# val = "antony 123 ;'"
# print (val)
# print (val[0])
# print (val[-1])



# name = "antony"
# print ("hello my name is {} joji".format(name))


name = 'antony'
place ='thodupuzha'
print ("hello my name is {0} joji and from {1}".format (name,place))
#or

print ("hello my name is {a} joji and from {b}".format (a=name,b=place))

#or
print(f"hello my name is {name} joji and from{place}")

# or

print("hello my name is %s joji and from %s"%(name,place))

#or
num=12.34234
print ("hello my name is %s joji and value %.2f"%(name,num))

#or
numb=1234
print ("hello my name is %s joji and my number is %d"%(name, numb))

##or
numbe=12.34
print ("hello my name is %s joji and value %f"%(name,numbe))

#or




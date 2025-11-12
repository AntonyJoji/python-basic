# File handling in Python
# x - create
# r - read
# w -write
# a -append
# b -binary

# 1 . open a file
# 2 .  operations
# 3. close the file

# #Opening a file
# file = open('text.txt', 'r') # or with open('text.txt') as file: so we don't need to close it manually
# print(file.name)
# print(file.mode)
# file.close()

# file = open('text.txt', 'r')
# # # # Reading from a file
# content = file.readlines()
# print(content)
# file.close()

# with open('text.txt','r')as file:
#     for line in file:
#         print(line,end='')/

# with open('text.txt','r')as file:
#     file_contents=file.read(75)
#     print(file_contents,end=" ")


# with open('text.txt','r')as file:
#     size_to_read=274
#     file_contents=file.read(size_to_read)

#     while len(file_contents)>0:
#         print(file_contents,end='')
#         file_contents=file.read(size_to_read)


# # Closing a file
# file.close()

# # Writing to a file
# file = open("text.txt", "w")
# file.write("Hello, World!\n")
# file.close()       
# 
# 
# 
# 
# 
# 
##tell() and seek()  method

# with open('text.txt','r')as file:
#     size_to_read=10
#     file_contents =file.read(size_to_read)
#     print(file_contents,end='')
#     file.seek(0)
#     file_contents = file.read(size_to_read)
#     print(file_contents)


###### writ mode##########

# with open('text1.txt','w')as file: 
#     file.write("hello hi this is first line ")


#########################################################################################################33

# File handling in Python
# x - create
# r - read
# w -write
# a -append
# b -binary

# 1 . open a file
# 2 .  operations
# 3. close the file


# f=open ('sample.text','w') ## w aka write modeill open chaithal existind condent rewrite aavoum but
# f.write("line number one \n")## if there is the specified file is not presnt it will automatically create the new file and write the data to the file 
# f.write("line number two \n")
# f.close()


# f=open ('sample.text','a')### a aka appent modill open chaithal rewrite avula but it will update the the file without overwriting
# f.write("line number one \n")
# f.write("line number two \n")
# f.close()


# f = open ('sample.text','r')
# data  =f.read()
# print(data)
# f.close()


###
#####read line  #####
# f=open ('sample.text','r')
# data = f.readlines()
# print(data)
# ls=[i.strip() for i in data]
# print (ls)
# new =[i[5:]for i in ls]
# print(new)  
# f.close()


# f = open ('sample.text','r')
# data  =f.readline()
# print(data)
# data  =f.readline()
# print(data)
# data  =f.readline()
# print(data)
# data  =f.readline()
# print(data)
# f.close()

# f = open ('sample.text','r')
# data  =f.readline()
# print(data)
# data  =f.readline()
# print(data)
# f.seek(0)## )(seek (0) the pointer will move to the 
# ############first line and start to read from the first
# #### if need to move to other point just need to mention the poninter eg seek(5) )
# data  =f.readline()
# print(data)
# data  =f.readline()
# print(data)
# f.close()

# f = open ('sample.text','r')
# data = f.readline()
# print (data)
# print(f.tell) ### (tell function is used to find the tell the corrent possition of the file pointer)
# data = f.readline()
# print (data)
# print(f.tell)
# data = f.readline()
# print (data)
# print(f.tell)
# data = f.readline()
# print (data)
# print(f.tell)
# f.close()



# f = open('det.jpg','rb') ## rb :=read binary
# data = f.read()
# print(data)
# f.close()


f = open('det.jpg','rb') ## rb :=read binary
data = f.read()
new =open('new_det.jpg','wb')## 'wb':= write binary ,is used to create a new copy of the file
new.write(data)
f.close()

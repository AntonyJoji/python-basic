# File handling in Python

# Opening a file
# file = open('text.txt', 'r') # or with open('text.txt') as file: so we don't need to close it manually
# print(file.name)
# print(file.mode)
# file.close()

# file = open('text.txt', 'r')
# # # Reading from a file
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

with open('text.txt','r')as file:
    size_to_read=10
    file_contents =file.read(size_to_read)
    print(file_contents,end='')
    file.seek(0)
    file_contents = file.read(size_to_read)
    print(file_contents)


###### writ mode##########

with open('text1.txt','w')as file: 
    file.write("hello hi this is first line ")



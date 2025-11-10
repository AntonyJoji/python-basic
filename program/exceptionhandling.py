try: #
    pass
except:#
    pass
finally:#
    pass

# num1= 10
# num2=0
# res=num1/num2
# print(res)


# print("completed")
# try:
#     num1= 10
#     num2=0
#     res=num1/num2
#     print(res)
# except:
#     print ("done")


# print("completed")

# try:
#     num1= int(input("enter the number1::"))
#     num2=int(input("enter the number2::"))
#     res=num1/num2
#     print(res)
# except:
#     print ("done")
# finally:
#     print("all good")
    
# print("completed")

# def div():
#     try:
#         num1= int(input("enter the number1::"))
#         num2=int(input("enter the number2::"))
#         res=num1/num2
#         print(res)
#     except:
#         print ("invalid entry ! please try again")
#         div()

# div()   
# print("completed")


# val =1
# while val ==1:
#     try:
#         num1= int(input("enter the number1::"))
#         num2=int(input("enter the number2::"))
#         res=num1/num2
#         print(res)
#         val =0
#     except:
#         print ("invalid entry ! please try again")
# print("completed")


try:
    num1= int(input("enter the number1::"))
    num2=int(input("enter the number2::"))
    res=num1/num2
    print(res)
except NameError:
    print ("Name error occurred!")
except ZeroDivisionError:
    print("ZeroDivitionError occurred!")
except:
    print("all done")
    
print("completed")






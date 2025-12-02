# class employee: ### blue print of object
#     pass

# obj1 = employee()## real time instance of class or object
# obj2 = employee()## real time instance

# print (obj1)
# print (obj2)


# class employees:
#     pass


# emp1 = employees()
# emp2 = employees()
# emp1.first ="david"
# emp1.last ="mathew"
# emp1.pay = 1000
# emp1.email ="danta@gmail.com"

# emp2.first ="david" 
# emp2.last ="mathew"
# emp2.pay = 1000
# emp2.email ="danta@gmail.com"

# print (emp1.first)


# class employees:
#     def __init__(self,first,middle=None,last=None,pay=None): ### constructor automatically called when we create object
#         self.first=first ## instance variable
#         self.last=last ## instance variable
#         self.middle=middle
#         self.pay=pay
#         self.email=first+last+"@gmail.com"## instance variable
#     def fullname(self):## 'self' is used to access instance variable and method inside the class
#            if self.middle is None:
#                 return self.first+" "+self.last
#            else:
#                 return self.first+" "+self.middle+" "+self.last
           
# emp1 = employees(first="david",last="mathew",pay=1000)# creating object and passing values to constructor
#  ## or when we create object constructor automatically called
# emp2 = employees(first="dainty",last="mathew",pay=4000)
# emp3 = employees(first="dan",middle='r',last='kumar',pay=5000)
# # print(emp1.email)
# # print(emp2.email)
# # print(emp1.last)

# print(emp1.fullname())
# print(emp2.fullname())
# print(emp3.fullname())


class employees:
    def __init__(self, first, last, pay, middle=None):
        self.first = first
        self.last = last
        self.middle = middle
        self.pay = pay
        self.email = first + last + "@gmail.com"

    def fullname(self):
        if self.middle is None:
            return self.first + " " + self.last
        else:
            return self.first + " " + self.middle + " " + self.last


first_name=input("enter the first name:")
middle_name=input ("enter the middle name (press enter if we need to skip):")
last_name=input("enter the last name:")
pay=int(input("enter the pay:"))

emp = employees(first=first_name,middle=middle_name,last=last_name,pay=pay)
print(emp.fullname())
print (emp.pay)
print(emp.email)
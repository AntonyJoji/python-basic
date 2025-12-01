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


class employees:
    def __init__(self,first,last,pay): ### constructor automatically called when we create object
        self.first=first ## instance variable
        self.last=last ## instance variable
        self.pay=pay
        self.email=first+last+"@gmail.com"## instance variable
        

emp1 = employees("david","mathew",1000)# creating object and passing values to constructor
 ## or when we create object constructor automatically called
emp2 = employees("dainty","mathew",4000)

print(emp1.email)
print(emp2.email)
print(emp1.last)




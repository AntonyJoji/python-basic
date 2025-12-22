## inheritance in python


# class A:
#     pass

# class B (A): ## A is parent class of B it means B is child class of A
#     pass

# class C (B): ## B is parent class of C it means C is child class of B
#     pass


# class employee:
#     raise_amt =1.04
#     def __init__(self,first,last,pay):
#         self.first =first
#         self.last =last
#         self.pay =pay
#         self.email = first+last+'@gmail.com'
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def raiseamount(self):
#         self.pay = int(self.pay * self.raise_amt)
# class developer(employee): ## developer is child class of employee
#     pass

# emp1 = employee("anto","john",50000)
# dev1 = developer("kiran","mohan",60000)
# print(dev1.fullname())
# print(dev1.raiseamount())


## yesterday's class 19/12/25

# class employee:
#     raise_amt =1.04
#     def __init__(self,first,last,pay):
#         self.first =first
#         self.last =last
#         self.pay =pay
#         self.email = first+last+'@gmail.com'
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def raiseamount(self):
#         self.pay = int(self.pay * self.raise_amt)
# class developer(employee):
#     raise_amt = 1.06
#     def __init__(self,first,last,pay,prog_lang):
#         super().__init__(first,last,pay) ## to call the parent class init method
#         self.prog_lang = prog_lang
# class manager(employee):
#     pass


########################

# print(issubclass(developer,employee)) ## to check whether developer is subclass of employee
# print(isinstance(dev1,developer)) ## to check whether dev1 is instance of developer
# print(isinstance(dev1,employee)) ## to check whether dev1 is instance of employee   
# print(isinstance(emp1,developer)) ## to check whether emp1 is instance of developer
# print(isinstance(emp1,employee)) ## to check whether emp1 is instance of employee

# class employee:
#     raise_amt =1.04
#     def __init__(self,first,last,pay):
#         self.first =first
#         self.last =last
#         self.pay =pay
#         self.email = first+last+'@gmail.com'
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def raiseamount(self):
#         self.pay = int(self.pay * self.raise_amt)
#     def __repr__(self):
#         return self.first
#     def __str__(self):
#         return f"{self.first} {self.last}"

# emp1 = employee("anto","john",50000)
# emp2 = employee("jose","mathew",60000)
# print(emp1)


# import datetime
# today =datetime.date.today()
# print(str(today))
# print(repr(today))

## operator overloading


# class employee:
#     raise_amt =1.04
#     def __init__(self,first,last,pay):
#         self.first =first
#         self.last =last
#         self.pay =pay
#         self.email = first+last+'@gmail.com'
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def raiseamount(self):
#         self.pay = int(self.pay * self.raise_amt)
#     def __repr__(self):
#         return self.first
#     def __str__(self):
#         return f"{self.first} {self.last}"
    
    # def __add__(self1,self2):
    #     return self1.pay+self2.pay
    # def __mul__(self1,self2):
    #     return self1.pay * self2.pay
    # def __len__(self):
    #     return len(self.fullname())-1

# emp1 = employee("anto","john",50000)
# emp2 = employee("jose","mathew",60000)

# print(emp1+emp2)
# print(emp1*emp2)
# print (len(emp1))


# class employee:
#     raise_amt =1.04
#     def __init__(self,first,last,pay):
#         self.first =first
#         self.last =last
#         self.pay =pay
#     def fullname(self):
#         return f"{self.first} {self.last}"
#     def email(self):
#         return f"{self.first}{self.last}@gmail.com"

# emp1 = employee("anto","john",50000)
# emp2 = employee("jose","mathew",60000)
# emp1.first = "kiran"

# print(emp1.first)
# print(emp1.email())
# print(emp1.fullname())

class employee:
    raise_amt =1.04
    def __init__(self,first,last,pay):
        self.first =first
        self.last =last
        self.pay =pay
    @property ## getter method it will act as attribute not as method
    def fullname(self):
        if self.first==None or self.last==None:
            return "name is deleted"
        return f"{self.first} {self.last}"
    @fullname.setter  ## setter method to set the value
    def fullname(self,name):
        first,last = name.split(" ")
        self.first = first
        self.last = last  
    @fullname.deleter 
    def fullname (self):
        print("delete name")
        self.first =None
        self.last =None              


    @property  ## getter method it will act as attribute not as method
    def email(self):
        return f"{self.first}{self.last}@gmail.com"

emp1 = employee("anto","john",50000)
emp2 = employee("jose","mathew",60000)
emp1.first = "kiran"

print(emp1.first)
print(emp1.email)  
print(emp1.fullname)

emp1.first = "rahul " #to change the first name
print(emp1.email)

emp1.fullname = "luck sharma" #to change the last name
print(emp1.fullname)


del emp1.fullname  ## to delete the fullname attribute
print(emp1.fullname)

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
#     @classmethod # decorator to define class method
#     def setraiseamt(cls,amount):
#         cls.raise_amt = amount

# emp1 = employee("anto","john",50000)
# emp2 = employee("jose","mathew",60000)
# employee.setraiseamt(1.05)
# print(employee.raise_amt)




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
#     @classmethod # decorator to define class method
#     def setraiseamt(cls,amount):
#         cls.raise_amt = amount
#     @classmethod
#     def setemps(cls,emp):
#         first,last,pay =emp.split('-') 
#         return cls(first,last,pay)

# emp1 = employee("anto","john",50000)
# emp2 = employee("jose","mathew",60000)
# employee.setraiseamt(1.05)
# print(employee.raise_amt)

# str1 ='kiran-mohan-70000'
# str2 ='raju-suresh-80000'
# str3 ='balu-dinesh-90000'

# emp3 =employee.setemps(str1)
# emp4 =employee.setemps(str2)
# emp5= employee.setemps(str3)
# print(emp3.fullname())
# print(emp4.fullname())
# print(emp5.fullname())



##### static method #####

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
#     @staticmethod ## decorator to define static method
#     def findday(day):
#         if day.weekday()==5 or day.weekday()==6:
#             return "it is a weekend"
#         else :
#             return "it is a weekday"

# emp1 = employee("anto","john",50000)
# emp2 = employee("jose","mathew",60000)

# import datetime
# date =datetime.date(2025,12,17)
# print(employee.findday(date))

##################################################

class Employee:
    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(projet_name):
        if projet_name =="ABC project":
            requriment = ['task1','task2','task3']
        else:
            requriment = ['task1']
        return requriment
    

    def work(self):
        requirments = self.gather_requirement(self.project_name)
        for task in requirments:
            print (f"completed {task}")


emp = Employee("kelly",100000,'ABC project')
emp.work()

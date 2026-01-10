# class animal:
#     def eat(self):
#         return "eating"
# class mammal(animal):
#     def walk(self):
#         return "walking"
# class bird(animal):
#     def fly(self):
#         return "flying"
# class bat(mammal,bird):
#     def sound(self):
#         return "bat make sounds"

# b = bat()
# b.eat()
# b.walk()
# b.fly()
# print(b.eat())
# print(b.walk())
# print(b.fly())
# print(b.sound())

#########polymorphism##########

## method overriding and method overloading

# class animal:
#     def eat(self):
#         print("eating") 
#     def walk (self):
#         print ("walking") 
# class mammal(animal):
#     pass
#     # def walk(self):
#     #     print("mammal walking")
#     def random(self,a=25,b=None,c=None):
#         if b:
#             return a*b
#         if c:
#             return c-5
#         return a*2

# m=mammal()
# # m.walk()
# print(m.random(c=10))


####################################3

# class animal:
#     def eat(self):
#         print("eating")
#     def _walk (self): ## sigle underscore indicates protected method
#         print ("walking")

# a= animal()
# a._walk()  ## can be accessed within the class and outside the class also but should be used within the class or subclass only


# class animal:
#     def eat(self):
#         print("eating")
#     def __walk (self): ## double underscore indicates private method
#         print ("walking")   

# a= animal()
# a.__walk()  ## cannot be accessed outside the class   



################################################

class person:
    __emp_type ='HR'
    def __init__(self,name,age,salary):
        self.name =name
        self._age =age  ## protected attribute use only within class and subclass
        self.__salary =salary ## private attribute cannot be accessed outside the class
    def show_salary(self):
        return self.__salary, self.__emp_type  ## accessing private attribute within the class


obj = person("anto",24,50000) ## instance attribution
print(obj.show_salary()) ## accessing private attribute using method within the class
print(obj.name)
print(obj._age)
#print(obj.salary)   ## cannot be accessed outside the class                    

print()





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

# class person:
#     __emp_type ='HR'
#     def __init__(self,name,age,salary):
#         self.name =name
#         self._age =age  ## protected attribute use only within class and subclass
#         self.__salary =salary ## private attribute cannot be accessed outside the class
#     def show_salary(self):
#         return self.__salary, self.__emp_type  ## accessing private attribute within the class


# obj = person("anto",24,50000) ## instance attribution
# print(obj.show_salary()) ## accessing private attribute using method within the class
# print(obj.name)
# print(obj._age)
# #print(obj.salary)   ## cannot be accessed outside the class                    

# # print(person.__emp_tpye) ## cannot be accessed outside the class


##########iterators and generators###############

# ls = [1,2,3,4] ## iterable object
# # for i in ls:
# #     print(i)  

# print(dir(ls)) 

# ls =[1,2,3,4]
# print(ls)
# val = iter(ls) ## creating iterator object using iter() function
# print(dir(val))
# print(next(val)) ## accessing elements using next() function
# print(next(val))## we have the control to access the elements
# print(next(val)) ##  iterator keeps track of the current position           
# print(next(val))

# ## or

# # for i in val:
# #     print(i)




# class myrange:
#     def __init__(self,start,end):
#         self.start =start
#         self.end =end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         current = self.start
#         self.start +=1
#         return current
           


# nums = myrange(1,10)
# # print(next(nums))
# # print(next(nums))
# # print(next(nums))

# ## or 

# for i in nums:
#     print(i)


###########generators###############


# def myrange (start):
#     current = start
#     while True:
#         yield current
#         current +=1

# res = myrange(5)
# print(next(res))
# for i in res:
#     print(i)
    


## example 

# def val():
#     yield 1
#     yield 2
# res = val()
# print(next(res))
# print(next(res))



## example2

# class myword():
#     def __init__(self,sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.word = self.sentence.split( )
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= len(self.word):
#             raise StopIteration
#         index = self.index
#         self.index += 1
#         return self.word[index]
    
    
# myobj = myword('hi i am devin mathew')
# print(next(myobj))
# print(next(myobj))
# print(next(myobj))
# print(next(myobj))  
# print(next(myobj))


# ## the simple way using generator function

# def mywords(sentence):
#     for word in sentence.split():
#         yield word

# obj = mywords("hello anto how are you")
# print(next(obj))
# print(next(obj))
# print(next(obj))        
# print(next(obj))
# print(next(obj))

########## abstract class ###########


from abc import ABC,abstractmethod
class vehicle(ABC):
    # def __init__(self):
    #     self.change_gear()
        
    def start_enginr(self):
        print("starting engine")
        
    def apply_break(self):
        print("applying break")
        
    def stop_engine(self):
        print("stopping the engine")
        
    @abstractmethod    
    def change_gear(self):
        print("changing gear maunally")
        
    
class car(vehicle):
    def open_sunroof(self):
        print("opening sunroof")
        
    def change_gear(self):
        print("changing gear maunally")
        
class truck(vehicle):
    def load_weight(self):
        print("loading weight")
        
    def change_gear(self):
        print("changing gear maunally")
# v = vehicle()
c = car()
t = truck()
# v.change_gear()
# c.change_gear()
# t.change_gear()




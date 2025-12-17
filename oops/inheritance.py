## inheritance in python


# class A:
#     pass

# class B (A): ## A is parent class of B it means B is child class of A
#     pass

# class C (B): ## B is parent class of C it means C is child class of B
#     pass


class employee:
    raise_amt =1.04
    def __init__(self,first,last,pay):
        self.first =first
        self.last =last
        self.pay =pay
        self.email = first+last+'@gmail.com'
    def fullname(self):
        return f"{self.first} {self.last}"
    def raiseamount(self):
        self.pay = int(self.pay * self.raise_amt)
class developer(employee): ## developer is child class of employee
    pass

emp1 = employee("anto","john",50000)
dev1 = developer("kiran","mohan",60000)
print(dev1.fullname())
print(dev1.raiseamount())

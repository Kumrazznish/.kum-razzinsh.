#multilevel inheritance
class employee():#Super class
    def __init__(self,name,age,salary):
       self.name = name
       self.age = age
       self.salary = salary
class childemployee1(employee):#child class
    def __init__(self,name,age,salary):
       self.name = name
       self.age = age
       self.salary = salary
class childemployee2(employee):#child class
    def __init__(self,name,age,salary):
       self.name = name
       self.age = age
       self.salary = salary
emp1 = employee('harshit',60,1000)
emp2 = childemployee1('arjun',50,2000)
print(emp1.age)
print(emp2.age)

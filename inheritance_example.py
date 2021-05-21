class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def work(self):
        return f"{self.name} is working"

class SoftwareEngg(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age)
        self.salary = salary
        self.level = level
        
    def coding(self):
        return f"{self.name} is coding"
    
class Designer(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        
    def designing(self):
        return f"{self.name} is designing"
    
sd = SoftwareEngg("Max", "29", 44000, "Senior")
dd = Designer("Lisa", 22, 24555)
 
print(sd.work())
print(sd.coding())

print(dd.work())
print(dd.designing()) 

'''
Output:
Max is working
Max is coding
Lisa is working
Lisa is designing
'''

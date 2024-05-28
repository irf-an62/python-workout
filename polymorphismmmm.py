'''polymorphism (polymorphism means the same function name,being used for different types)

#this can do both 2 fun(a+b & a+b+c)

def add(a,b,c=2):
    print(a+b+c)
add(12,45,4)
add(2,4)  '''


'''polymorphism example
class animal():
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dod barks")

class bird(animal):
    def sound(self):
        print("Birds sing")

d1=bird()
d1.sound()
             '''

''' example 1 polymor


class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self):
        l=10
        b=30
        print(l*b)

r=rectangle()
r.area()            '''


''' examp 3 polymor

class vehicle():
    def start(self):
        print("vehicl started")

class car(vehicle):
    def start(self):
        print("car started")


c=car()
c.start()   '''



class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(Employee):
    def __init__(self,department):
        self.department=department

        
    def display(self):
        print(self.name,self.salary,self.department)

m=manager()
m.display()
        
    


        

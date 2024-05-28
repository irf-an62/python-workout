'''class and object example


class laptop:
    price=0
    processor=""
    ram=""

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=50000
hp.processor="i3"
hp.ram="6gb"

dell.price=70000
dell.processor="i5"
dell.ram="8gb"

lenovo.price=90000
lenovo.processor="i7" 
lenovo.ram="12gb"

print(hp.price)
print(dell.price)
print(lenovo.price)  '''


'''using constructor in class and self keyword  (not much understand)
class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)

hp=laptop()#object

hp.ram="6gb"
hp.processor="i3"

hp.display()   '''




#tried something understand
'''
class student:
    def __init__(self):
        self.name="irfan"
        self.regno="2468"
    def display(self):
        print("name:",self.name)
        print("reg no:",self.regno)


s1=student()
s2=student()

s1.name="irfan"
s1.regno="1"

s2.name="ahmed"
s2.regno="2"

s1.display()
s2.display()   
'''


''' constructor exmplsssss
class fruit:
    def __init__(self,col):
        self.color=col

     
apple=fruit("pink")
print(apple.color) '''



''' using  constructor
class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("name:", self.name) 
        print("reg no:", self.regno) 


t1=teacher("irfan","1")
t2=teacher("ahmed","2")

t1.display()
t2.display()      '''


'''
class calculator:
     def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add:",self.num1+self.num2)
    def sub(self):
        print("sub:",self.num1-self.num2)
    def mul(self):
        print("mul:",self.num1*self.num2)
    def div(self):
        print("div:",self.num1/self.num2)    

obj1=calculator(10,2)
obj1.add()

obj2=calculator(10,2)
obj2.sub()

obj3=calculator(10,2)
obj3.mul()

obj4=calculator(10,2)
obj4.div()   '''


      



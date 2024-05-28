#single inheritance:
'''
class a:
    def fun1(self):
        self.a=input('name:')
        self.b=int(input('mark:'))

class b(a):
    def fun2(self):
        print(self.a,self.b)

obj=b()
obj.fun1()
obj.fun2()'''


'''
class A:
    def __init__(self):
        print('jdhd')
    def __init__(self):
        print('jd')
    def __init__(self):
        print('jdw')

obj1=A()
obj2=A()
obj3=A()   '''



#task:

'''
class A:
    def fun1(self):
        for i in range(4):
            self.name=input('enter the name:')
            self.age=int(input('enter the age:'))
            self.dob=int(input('enter the D.O.B:'))

class B(A):
    def fun2(self):
        data.fun1()
        print(self.name,self.age,self.dob)
        

data=B()
data.fun2()'''


#multiple inheritance:::;
'''
class a:
    def fun1(self):
        self.a=input('patient name:')

class b:
    def fun2(self):
        self.b=int(input("enter the age:"))

class c(b,a):
    def display(self):
        obj.fun1()
        obj.fun2()
        print(self.a,self.b)

obj=c()
obj.display()'''


#example:
'''
class a:
    def get_details(self):
        self.studentid=int(input('enter the id:'))
        self.studentname=input('enter the name:')

    def display(self):
        print(self.studentid,self.studentname)

class b:
    def school(self):
        self.school=input('enter the school name:')
    def schooldisplay(self):
        print(self.school)

class c(a,b):
    def displayall(self):
        obj.get_details()
        obj.school()
        obj.display()
        obj.schooldisplay()
        obj.displayall()


obj=c()
obj.displayall()'''

class A:
    def get_details(self):
        self.studentid = int(input('Enter the id: '))
        self.studentname = input('Enter the name: ')

    def display(self):
        print(self.studentid, self.studentname)

class B:
    def school(self):
        self.schoolname = input('Enter the school name: ')

    def schooldisplay(self):
        print(self.schoolname)

class C(A, B):
    def displayall(self):
        self.get_details()  # Use self to access methods from parent classes
        self.school()
        self.display()
        self.schooldisplay()

obj = C()
obj.displayall()

        

#class and object:: 
'''
class name():
    def hi(self):
        print("irfan")
    def hloo(self):
        print("ahmed")
    def olo(self):
        print("fawaz")


fname=name()
fname.hi()
fname.hloo()
fname.olo()'''



#sir teachedddd
'''
class A:
    def fun(self):
        self.a=int(input('enter the num:'))
        b=20
    def fun2(self):
        print(self.a)
        print(b)


obj=A()

obj.fun()
obj.fun2()  '''


'''
class A:
    def fun1(self):
        self.a=input('name')
        self.b=int(input('age'))

    def display(self):
        print(self.a,self.b)

obj1=A()
obj2=A()
obj1.fun1()
obj2.fun1()
obj1.display()
obj2.display()'''



#task
'''
class arithmetic:
    def add(self):
        self.a=int(input("enter the num1:"))
        self.b=int(input("enter the num2:"))
        print(self.a+self.b)

    def sub(self):
##        self.a=int(input("enter the num1:"))
##        self.b=int(input("enter the num2:"))
        print(self.a-self.b)

    def mul(self):
##        self.a=int(input("enter the num1:"))
##        self.b=int(input("enter the num2:"))
        print(self.a*self.b)

    def div(self):
##        self.a=int(input("enter the num1:"))
##        self.b=int(input("enter the num2:"))
        print(self.a%self.b)

operator=arithmetic()
operator.add()
operator.sub()
operator.mul()
operator.div()'''



#taskk
'''
class task:
        def data(self):
                for i in range(1,5):
                    self.a=input('name:')
                    self.b=input('location:')
        def display(self):
            self.c=input("enter your name:")
            print(self.c)


obj=task()
obj.data()
obj.display()'''

          #altereddd  

'''
class Task:
    def __init__(self):
        self.data_list = []  

    def data(self):
        for i in range(1, 5):
            name = input('Enter your name: ')
            location = input('Enter your location: ')
            self.data_list.append({'name': name, 'location': location}) 

    def display(self):
        self.c = input("Enter your name: ")
        for data_entry in self.data_list:
            if data_entry['name'] == self.c:
                print(f"Name: {data_entry['name']}")
                print(f"Location: {data_entry['location']}")
                break
        else:
            print("Name not found in the data.")

obj = Task()
obj.data()
obj.display()'''



       #or

'''
a=[]
class b:
    def fun1(self):
        for i in range(n):
            self.name=input('enter the name:')
            self.location=input('enter the location:')
            a.extend(self.name,self.location)


    def fun2(self):
         b=input('enter the name to search:')
         for i in range(len(a)):
             if a[i]==b:
                 print(a[i],a[i+1])

n=int(input())
obj=b()
obj.fun1()
obj.fun2()'''



#task (1/11/23)

'''        
          
class Task:
    def __init__(self):
        self.data_list = []  

    def data(self):
        for i in range(1, 5):
            name = input('Enter your name: ')
            disease = input('Enter your disease: ')
            self.data_list.append({'name': name, 'disease':disease}) 

    def display(self):
        self.c = input("Enter your name: ")
        for data_entry in self.data_list:
            if data_entry['name'] == self.c:
                print(f"Name: {data_entry['name']}")
                print(f"disease: {data_entry['disease']}")
                break
        else:
            print("Name not found in the data.")

obj = Task()
obj.data()
obj.display()  '''




#super methodd::::
'''
class A:
    def __init__(self):
        self.a=input('student name:')
        self.b=int(input('mark:'))

class B(A):
    def __init__(self):
        super().__init__()
        self.c=input('school name:')

    def display(self):
        print(self.a,self.b,self.c)


obj=B()
obj.display()'''



#taskk: 06/11/23(student database(administration and student data):)
'''
class StudentDatabase:
    student_info = []

    def __init__(self):
        for i in range(1,5)
            self.name = input('Enter the name: ')
            self.regnum = int(input('Enter the regnum: '))
            self.dob = int(input('Enter the dob: '))
            self.englishmark = int(input('Enter the English mark: '))
            self.tamilmark = int(input('Enter the Tamil mark: '))
            self.mathsmark = int(input('Enter the Maths mark: '))
            self.sciencemark = int(input('Enter the Science mark: '))
            self.socialmark = int(input('Enter the Social mark: '))

            total = self.englishmark + self.tamilmark + self.mathsmark + self.sciencemark + self.socialmark
            print('Total Marks:', total)

            self.student_info.append({
                'name': self.name,
                'regnum': self.regnum,
                'dob': self.dob,
                'englishmark': self.englishmark,
                'tamilmark': self.tamilmark,
                'mathsmark': self.mathsmark,
                'sciencemark': self.sciencemark,
                'socialmark': self.socialmark,
                'total': total
            })

class A:
    def data(self):
        self.regnum = int(input('Enter the regnum to search: '))
        self.dob = int(input('Enter the dob to search: '))


    def validate(self):
        
        for student in StudentDatabase.student_info:
            if student['regnum'] == self.regnum and student['dob'] == self.dob:
                return student

class B(A):
    def display(self):
        student_data = self.validate()
        if student_data:
            print('Regnum:', student_data['regnum'])
            print('DOB:', student_data['dob'])
            print('English Mark:', student_data['englishmark'])
            print('Tamil Mark:', student_data['tamilmark'])
            print('Maths Mark:', student_data['mathsmark'])
            print('Science Mark:', student_data['sciencemark'])
            print('Social Mark:', student_data['socialmark'])
            print('Total Marks:', student_data['total'])
        else:
            print('Invalid Regnum or DOB')

obj1 = StudentDatabase()
obj2 = B()

while True:
    obj2.data()
    obj2.display()
    choice = int(input('Enter 1 to continue or 2 to exit: '))
    if choice == 2:
        break  '''



#hierarchical inheritance..

'''
class bank:
    def bank(self):
        self.bankname="SBI Bank"
        self.address="No.1,koyambedu"

class employee(bank):
    def employee(self):
        self.employeename=input()
        print(self.bankname,self.address,self.employeename)

class customer(bank):
    def customer(self):
        self.customer=input()
        print(self.bankname,self.address,self.customer)


obj1=employee()
obj2=customer()
obj1.bank()
obj2.bank()
obj1.employee()
obj2.customer()'''



#Encapsulationnn::
'''
class a:
    def fun1(self):
        self.a=10
        self.__b=20
        self._c=30

obj=a()
obj.fun1()
print(obj.a)
print(obj._c)        
print(obj.__b)  '''  



#name manglingg:

'''
class a:
    def fun1(self):
        self.__a=input("age:")

    def __fun2(self):
        print('private method')

    def __fun3(self):
        self.__b=10
        self._c=20
        self.d=30

obj=a()
obj.fun1()
obj._a__fun2()

obj._a__fun3()   #both not printttt 
obj_a.__a  '''


#polymorphismm:

#opertaor overloadingg:

'''
class a:
    def __init__(self,x,y):
        self.m=x
        self.n=y

    def __add__(other,new):
        print(other.m+new.m)
        print(other.n+new.n)

obj1=a(5,10)
obj2=a(20,30)  
obj1+obj2 '''



#examplee

'''
class A:
    def __init__(self,x,y):
         self.m=x
         self.n=y

    def __add__(self,new):
        a=self.m+new.m
        b=self.n+new.n
        return A(a,b)

    def __sub__(other1,other2):
        a=other1.m-other2.m
        b=other1.n-other2.n
        return A(a,b)
        

obj1=A(5,10)
obj2=A(20,30)
obj3=obj1+obj2
obj4=obj1-obj2
print(obj3.m,obj3.n)
print(obj4.m,obj4.n)   '''


'''
class A:
    def __init__(self,x,y):
         self.m=x
         self.n=y

    def __add__(self,new):
        a=self.m+new.m
        b=self.n+new.n
        return A(a,b)

    def __sub__(other1,other2):
        a=other1.m-other2.m
        b=other1.n-other2.n
        return A(a,b)
        

obj1=A(5,10,20,30)
obj2=A(20,30.40,50)
obj3=obj1+obj2+obj3+obj4
obj4=obj1-obj2
print(obj3.m,obj3.n)
print(obj4.m,obj4.n)  '''


#abstrationnn::

'''
from abc import ABC,abstractmethod

class A(ABC):
    def fun1(self):
        print("it is abstract method,but not abstract method")


obj=A()
obj.fun1()'''


'''
from abc import ABC,abstractmethod

class A(ABC):
    def fun1(self):
        print("abstract method")


class B(A):
    def fun2(self):
        print('derived class')

obj=B()
obj.fun1()
obj.fun2()'''



'''
from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def fun1(self):
        print("it is abstract method,but not abstract method")

                     #it will not workkkkk
obj=A()
obj.fun1() '''
        



from abc import ABC,abstractmethod

class A(ABC):
    def fun1(self):
        print("method 1")

    @abstractmethod
    def fun2(self):
        print('method 2')


class B(A):
    def fun2(self):
        #super().fun2()           #ipd potta innoru fun2 call pannlmmmm
        print('derived class')

obj=B()
obj.fun1()
obj.fun2()





    
        

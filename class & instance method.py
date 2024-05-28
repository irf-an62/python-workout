'''
#class method:

class student:
    name="irfan"
    age=21

    def print():
        print("name:",student.name)
        print("age:",student.age)

student.print() '''       


'''
#instance method:

class student:
    name="irfan"
    age=21

    def print(self):
        print("name:",student.name)
        print("age:",student.age)


o=student()
o.print()  #or
student.print(o)'''


#__init__ method or constructor

class user:
    def __init__(self):
        print("call when new instance created")

o=user()
o1=user()        
o2=user()        



'''
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.msg=self.name + "is" + str(self.age) + "years old"


o=user("irfan ahmed",22)
print(o.name)
print(o.age)
print(o.msg)  '''


#oru constructor vachi oruka dha edit panna mudiyumm so this typ::::
'''
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #self.msg=self.name + "is" + str(self.age) + "years old"

    @property
    def msg(self):
        return self.name + "is" + str(self.age) + "years old" 

        
o=user("irfan ahmed",22)
print(o.name)
print(o.age)
print(o.msg)
o.age=25
print(o.msg)'''




'''
#property decorators getter setter::(not undwrstand )#wrong

class student:
    def __init__(self,total):
        self.total=total

    def average(self):
        return self.total/5.0


o=student(450)
print("total:",o.total)
print("average:",o.average())

o.total=(250)
print("total:",o.total)
print("average:",o.average())'''

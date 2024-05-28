#class attribute:
'''
class student():
    name="irfan"
    age=21'''
'''
#getattr method:

print(getattr(student,'name'))
print(getattr(student,'age'))'''



'''
#dot notation method:

print(student.name)
print(student.age)'''


#instance attribute:
     #(For every object, a separate copy of the instance variable will be created)

class user:
    course="java"


o=user()
print(user.course)#class attribute
print(o.course)#both are same

o.course="python"
print(o.course)#instance variable

o2=user()
print(o2.course)



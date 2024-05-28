'''qn:1 in function

def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()    
    
def sub():
    a=int(input())
    b=int(input())
    print(a-b)
sub()  '''

'''funct using evn or odd num
def findevenorodd():
        if(a%2==0):
             print("even")
        else:
             print("odd")
a=int(input("enter:"))             
findevenorodd()   '''


'''fun finding pass or fail
def findpassorfail():
    if(a<=35):
        print("fail")
    else:
        print("pass")
a=int(input("enter the num:"))  
findpassorfail()  '''



#finding range in fun
'''
def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
a=int(input("enter a:"))
b=int(input("enter b:"))
printrange(a,b) '''  


#tutor joes functionnn
'''
def welcome():
    print("welcme to my home")

welcome()
welcome() '''



#return typ wthout argument
'''
def mul():
    a=int(input("enter the num a:"))
    b=int(input("enter the num b:"))
    c=a*b
    return c


x=mul()
print(x)   '''



'''
#arbitrary argument(*)

def lass(*student):
    print(student)

lass("apple","mango","cat","dog")'''


'''
#arbitrary keyword


def school(**teacher):
    print(teacher)

school(name="subaa",age=34,gender="female",place="chl",behaviour="not bad") '''

'''2
#default prameter

def user(name,city="chl"):
    print(name,"is from",city)

user("irfan","colachel")
user("irfan")'''


'''
#passing an list in function

def total(marks):
    return sum(marks)

print("Total:",total([23,56,78,90,32,56]))  '''



'''
#lamba function

c=lambda a:a+50
print(c(5))'''


'''
c=lambda a,b,c:a*b*c
print(c(1,3,6))'''




'''   
def oddoreven(number):
    if (number // 2) * 2 == number:
        print("Even")
    else:
        print("odd")
        

a = int(input("Enter a number: "))
oddoreven(a)'''

         #(or)

'''
def oddoreven(number):
    if number & 1:
        print("Odd")
    else:
        print("Even")

a = int(input("Enter a number: "))
oddoreven(a)'''


   


'''
def registration(password):
    if len(password) >= 8 and any(char.isdigit() for char in password):
        print("Registration successful")
    else:
        print("Registration unsuccessful")

reg_username = input("Enter the username: ")
reg_password = input("Enter the password: ")

def login():
    log_username = input("Enter the username: ")
    log_password = input("Enter the password: ")
    if reg_username == log_username and reg_password == log_password:
        print("Validation successful")
    else:
        print("Validation unsuccessful") 

registration(reg_password)
login()  '''



'''
def outer():
    name=input("enter a name:")
    def inner():
        age=int(input("enter the age:"))
        print("Name:", name)
        return age
    age=inner()
    print("Age:", age)
    return name,age
def fun3():
    location=input("enter the location:")
    name,age=outer()
    print("Location:", location)
    
fun3()'''





'''
a = [1, 2, 3, 4, 5]
b = [6, 7, 8]
c = [9, 10, 11, 12]

d=map(lambda x,y,z:x+y+z,a,b,c)
print(list(d))'''



a = [1, 2, 3, 4, 5]
b = [6, 7, 8]
c = [9, 10, 11, 12]

# Use list comprehension to add corresponding elements from a, b, and c
result = [x + y + z for x, y, z in zip(a, b, c)]

# Print the resulting list
print(result)








    

        





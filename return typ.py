'''

#return type example

s_username="irfan"
s_password="1234"

uname=input("Enter value for username:")
password=input("Enter value for password:")

def validate():
    if(s_username==uname and s_password==password):
        return True
        #print("correct")
    else:
        return False
        #print("wrong")
a=validate()
print(a)     '''


#(a+b)*c             
'''
def add(n1,n2):
    return n1+n2

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

added=add(a,b)

output=added*c

print(output)'''



''' getting an input:

a=int(input("enter a num:"))
b=int(input("enter a num:"))
c=int(input("enter a num:"))
d=a+b+c
print()        '''




''' giving multiple inputs in single line:

name1,name2,name3=input("enter 3 name:").split(",")
print("name1:",name1)
print("name2:",name2)
print("name3:",name3) '''


''' avoiding [] in output:

a=["23,45,67"]
print(','.join(a))  '''


#string and string functions

'''
a="irfan ahmed mohamed nooh"
print(a)
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.count("a"))
print(a.endswith("o"))
print(a.find("r"))
print(a.replace("o","0"))
print(a.split())           '''



'''
#string manipulation:

s a m p l e
0 1 2 3 4 5
-6-5-4-3-2-1


s="sample"
print(s)
print(s[0:3])#to print frst three letter
print(s[5])#to print exact only one num
print(s[:4])#to print frst and given  num
print(s[1:])#to print xept frst letter
print(s[::-1])#to reverse a word            '''

'''

#arithmetic operator
 
a = 23
b = 10

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division (floating-point result)
print(a // b) # Integer Division (floor division)
print(a % b)  # Modulus (remainder)
print(2 ** 3) # Exponentiation     '''


'''

#assignment operator

a=24
print(a)
a+=6   #a=a+5
print(a)
a-=6   #a=a-5
print(a)
a*=6   #a=a*5
print(a)
a/=6   #a=a/5
print(a)
a%=6   #a=a%5
print(a)
a**=6   #a=a**5
print(a)                '''


'''
#comparision operators or relational operators

a=10
b=20

print(a==b)  #== equal
print(a!=b)  #!=not equal
print(a>b)  #>greater than
print(a<b)  #<lesser than
print(a>=b)  #>=greater than or equal to
print(a<=b)   #<= less than or equal to      '''


'''
#logical operator

AND
OR
NOT   '''

'''
#bitwise operator

...........


#if statement
......


#nested if
.....

'''


'''
        //#loooping statemnt
        
#while loop
i=2
while i<=20:
    print(i)
    i+=2       '''


'''   
#continue statement
i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue
    print(i)
    i+=1     '''

'''
#break statement
i=1
while i<=20:
    if i==9:
        break
    print(i)
    i+=1      '''

'''
for i in range(5):
    a=int(input("enter a num a:"))
    b=int(input("enter a num b:"))
    print(a+b)  '''



'''
#nested for loop(ex and important intervieww)

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")        '''



'''
#tuple

x=('irfan',)*10
print(x)             '''


#set
name={"rahumath","nooh","ahmed","irfan"}
print(name)
  

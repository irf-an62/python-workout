'''

a=[1,2,3,4]
#a.append(5)
#a.insert(2,6)
#b=a.copy()
b=a.index(4)
print(b)'''



'''
a=[]
for i in range(100):
    n=int(input("enter a num:"))
    a.append(n)
    if n==0:
        break
print(a) '''



'''
#printing odd and even numbrs:
a=[]
b=[]
for i in range(1,101):
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
print(a)        
print(b)'''



'''
a=[10,20,30,50,7,3,100]
b=a.index(50)
c=a.index(3).
d=b+c
print(d)'''

'''
#class task:

a=[10,20,30,50,7,3,100]

for i in a:
    if i!=7:
        print(i)  '''    


'''
a=[]
b=0
c=1
d=b+c
for i in range(10):
    print(b)
    b=c
    c=d
    d=b+c
print(a) '''




'''
a = []
b = 0
c = 1
for i in range(10):
    if i % 3 != 2:  # Skip every third element
        a.append(b)
    print(b)
    b, c = c, b + c
print(a)'''


'''
a=[1,2,3,[4,5,6],7,8]
a[3].insert(3,9)
print(a)'''


'''
a=[6,5,4,3,2,1,2.5]
a.sort()
print(a)'''


'''
a=[21,34,5,67,78,65]
#print(max(a))
#print(min(a))'''


'''
a=["fawaz","ahmed","irfan"]
#print(max(a))
#print(min(a))'''


'''
#task:(to print a smallest list among a list)

a=[1,2,3,[5,6],[5],[7,8],[9,1,2]]
b=[]
for i in a:
    if type(i)==list:
        b.append(i)
        c=min(b,key=len)
print(c) '''






        



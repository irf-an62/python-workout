'''
a=lambda x:x+2
print(a(5))
print(a(7))'''


'''
a=lambda x,y:x+y
print(a(3,4))
print(a(5,6))'''


'''
a=[1,2,3,4,5]
b=[]
for i in a:
    n=lambda x:x*x
    b.append(n(i))

print(b)    '''


#task



'''
def add():
    a=[1,3,7,10,20,50]
    b=len(a)-1
    for i in range(b):
        z=lambda x,y:x+y
        print(z(a[i],a[i+1]))
add()'''


'''
def add():
    a = [1, 3, 7, 10, 20, 50]
    b = len(a) - 1
    result = []
    for i in range(b):
        z = lambda x, y: x + y
        result.append(z(a[i], a[i + 1]))
    return result

output_list = add()
print("Output List:", output_list)'''


#filter function
'''
def fun1(x):
    if x>5:
        return x*x
a=[1,2,10,15,20]
b=list(filter(fun1,a))
print(b)'''




'''
def fun(x):
    if len(x)>=5:
        return x
a=[]
for i in range(5):
    b=input("enter name")
    a.append(b)
c=list(filter(fun,a))
print(c)'''


#closure function
'''
def outer(m):
    print(m)
    def inner(n):
        print(n)
        return m+n

    o=inner
    return o

a=outer(1)
b=outer(2)
print(a(3))
print(b(4))
print(a(b(5)))
print(b(a(6)))
print(a(b(a(7))))'''



#task(5&6 table)

'''
def outer(x):
    def inner(y):
        return x*y
    return inner
a=outer(5)
b=outer(6)
for i in range(1,11):
    print(i,"x","5","=",a(i),end=" ")
    print(i,"x","6","=",b(i))'''



#iterator:
'''
a='irfan'
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))'''




#generator:
'''
def fun(x):
    for i in range(1,x+1):
        yield i

a=fun(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))'''


         #task
'''
a=['hlooo','ahmed','30','16.4','irfan']
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))'''


#recursion
'''
def fun(x):
    if x==1:
        return 1
    else:
        return x*fun(x-1)
n=int(input("entera num:"))
print(fun(n))'''



#zip functionn:
''''
a=[1,2,3,4,5]
b=['irfan','ahmed','fawaz','nooh','rahmath']
c=zip(a,b)
#print(list(c))
print(tuple(c))'''

#enumerator function:
'''
a=['don','irfan','ahmed','raja','gowshi']
#print(list(enumerate(a)))
#print(list(enumerate(a,3)))
for i in enumerate(a):
    print(i)

for j,i in enumerate(a,start=4):
    print(j,i)'''



#task
'''
# Sample input of 12 players (6 batters and 6 bowlers) with their scores
players = [
    {"name": "Batter1", "score": 50},
    {"name": "Batter2", "score": 65},
    {"name": "Batter3", "score": 42},
    {"name": "Batter4", "score": 70},
    {"name": "Batter5", "score": 55},
    {"name": "Batter6", "score": 48},
    {"name": "Bowler1", "score": 3},
    {"name": "Bowler2", "score": 5},
    {"name": "Bowler3", "score": 2},
    {"name": "Bowler4", "score": 6},
    {"name": "Bowler5", "score": 4},
    {"name": "Bowler6", "score": 7}
]

# Separate batters and bowlers
batters = [player for player in players if player["name"].startswith("Batter")]
bowlers = [player for player in players if player["name"].startswith("Bowler")]

# Sort batters and bowlers by score in descending order
sorted_batters = sorted(batters, key=lambda x: x["score"], reverse=True)
sorted_bowlers = sorted(bowlers, key=lambda x: x["score"], reverse=True)

# Print highest batters one by one
print("Highest batters:")
for batter in sorted_batters:
    print(batter["name"], "-", batter["score"])

# Print highest bowlers one by one
print("\nHighest bowlers:")
for bowler in sorted_bowlers:
    print(bowler["name"], "-", bowler["score"])'''



#decorator

def outer(fun):
    def inner():
        print('before decorator')
        fun()
        print('after decorator')
    return inner   
        

@outer
def new():
    print('decorator statement')

new()    






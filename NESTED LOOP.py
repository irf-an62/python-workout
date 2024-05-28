''' 
for i in range(1,6):
    for j in range(1,3):
        print(j,"apple")'''

'''
for i in range(1,3):
    print("week:",i)
    for j in range(1,4):
        print("Day:",j)'''

'''
for i in range(1,5):
    print()
    for j in range(1,i+1):
          print(j,end="") '''




'''
for i in range(1,100):
    n=int(input())
    if n==0:
        break
print("loop ended") '''


'''
for i in range(5,-5,-1):
    print(i)  '''


'''
for i in range(1,5):
    print(range(i))'''
 



''' task: (when 0 it will break balance then value will add give total)

total = 0
while True:
    a = int(input("Enter a number: "))  
    if a == 0:
        break  
    total += a
print("Total:", total)
         '''
                                #(or)

'''

count=0
sum=0
for i in range(100):
    n=int(input("enter the num:"))
    if n==0:
        break
    sum=sum+n
    count=count+1

print("total",sum)
print("count",count)        '''



'''
count=0
sum=0
for i in range(100):
    n=int(input("enter the num:"))
    if n==0:
        continue
    sum=sum+n
    count=count+1
    if n==0:
        break

print("total",sum)
print("count",count)  '''



'''

count = 0
sum = 0
zero_count = 0

for i in range(100):
    n = int(input("enter the num:"))
    
    if n == 0:
        zero_count += 1
        if zero_count == 2:
            break  
    else:
        sum += n
        count += 1

print("total", sum)
print("count", count)     '''




#prime numbers between(10-100)
'''
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)   '''



''' sir given

for i in range(-5,5,5):
    print(i)
    for j in range(5,10):
        print(i,j)
    print("j loop ended")  '''


'''
for i in range(0,1):
    print("i loop")
    for j in range(10,15,2):
        print("j loop")
print("i loop ended") '''


'''
for i in range(5):
    for j in range(i):
        print(i)
    print(i)   '''



'''
for i in range(1,5):
    for i in range(i):
        print(i)  '''



'''
for i in range(-5,0):
    for j in range(i,-1):
        print(i,j)
        for k in range(i,j):
            print(i,j,k)    '''


'''
a=5
i=3
for i in range(i,i+3,i+2):
    print(i*a)
    for j in range(a,i*i,i+1):
        print(i*j,j*i)           '''


'''
for i in range(1,3):
    for j in range(2,5):
        for k in range(7,8):
            print(i,j,k)   '''

'''
for i in range(7,10,2):
    for j in range(5,10,2):
        for k in range(i,i+j):
            print(i,j,k)        '''

'''
for i in range(1,6):
    print("*" * i)  '''


'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==1 or i==5 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()                        '''


'''
count=1
for i in range(1,5):
    for j in range(1,i+1):
        print(count,end=" ")
        count=count+1
    print()    '''



'''
for i in range(-5,-1,-2):
    for i in range(i,-i):
        print(i)
        for j in range(i,i+i,i+i):
            print(i,j)
    print(i)             '''


'''
i=5+2
for i in range(-10,5,10):
    print("i")
    for j in range(i*i,i*i):
        print(j)    '''



''' 
for i in range(1,10,5):
    for j in range(-5,-3):
        for k in range(1,3):
            for l in range(10,12):
                print(i,j,k,l)         '''



#task
   

for i in range(5,0,-1,):
    for j in range(i,0,-1):
        print('*',end=" ")
    print()    

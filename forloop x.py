'''  creating 2nd8 table
for i in range(1,11):
    print(i,"x2=",i*2)'''

''' creating 3nd table
for i in range(1,11):
    print(i,"x3=",i*3)'''

'''forloop eg (qn-1)

a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)'''

'''putting if on forloop:
for i in range(1,11):
    if(i%2==0):
      print(i)'''

'''count check for even no 
count=0
for i in range(1,5):
    if(i%2==0):
        count=count+1
print(count)'''

'''count for evn and odd num
evn_count=0
odd_count=0
for i in range(1,11):
    if(i%2==0):
        evn_count=evn_count+1
    else:
        odd_count=odd_count+1
print(evn_count)
print(odd_count)'''


'''count a num which are divisible by 3 & 5
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)'''

'''compute sum of frst 5 natural nums
sum=0
for i in range(1,6):
    sum=sum+i
print(sum) '''


'''
a=[1,2,3,4,5,6,7,8,]
for i in a:
    print(i)'''

'''
a=[]
for i in range(10):
    num=int(input())
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)  '''


'''
for i in range(0,11,3):
    print(i)   '''



'''
a=int(input("enter a num"))
for i in range(a):
        print(i,end=" ")
    #print(i,end="5")         '''


'''
#ex for loop concept in interview

for i in range(1,6):
    print("*"*i)
                  '''

'''
a='irfan'
for i in range():
    print(a)    '''



for i in range(1,10):
    print(i)
    if i>5:
        break
else:
    print("for loop ended")

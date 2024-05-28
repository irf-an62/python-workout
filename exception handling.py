''' name error 

print("hi")
print("hloo")
printt("do wht")  '''


''' value error

a=int(input())
b=int(input())
print(a+b)     '''



'''type error

a=int(input())
b=int(input())
c=input()
print(c/a)   '''



'''handling error

try:
    a=int(input())
    b=int(input())
except ValueError as e:
    print("Value Error",e)
except Exception:
    print("something Wrong")
finally:
    print("done")   '''




#class workout:
#example 1
'''
try:
    a=int(input())
    b=int(input())
    c=a/b
except ZeroDivisionError:
    print("cannot divide")

else:
    print(c)

finally:
    print("program ended") '''






    
    

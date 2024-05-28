#try block in python

# try:
#     a=10/0
# except Exception as e:
#     print(e)

'''
try:
    a=10/5
except Exception as e:
    print(e)
else:
    print("a value is:",a)'''


'''  
try:
    a=10/5
except Exception as e:
    print(e)
else:
    print("a value is:",a)
finally:
    print("thank you")'''


#types of exceptions

   # print(dir(locals()['__builtins__']))  (yavlo erkk nu paaka)
   #  print(len(dir(locals()['__builtins__'])))



#Nameerror exception:

# try:
#     print(a)
# except NameError:
#     print("a is not defined")

'''
#zero division error:
    
try:
    print(10/0)
except ZeroDivisionError :
    print("denominator can't be zero")   '''


#value error:
# try:
#     a=int("irfan")
# except ValueError :
#     print("pls enter num only")


'''
#index error:
try:
    a=[1,2,3,4,5,6,7]
   # print(a[0])
    print(a[10])
except IndexError :
    print("invalid index")'''

'''
#file not found error:

try:
    a=open("test.txt")
except FileNotFoundError :
    print("file not found")
else:
    print(f.read())'''

   


    

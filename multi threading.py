#threading is which is running multiple fun at a time

import threading
#import time
#start=time.time
def fun1():
    for i in range(5):
        print("thred 1",i)


def fun2():
    for j in range(5):
        print("thread 2",j)


a=threading.Thread(target=fun1())        
b=threading.Thread(target=fun2())

#end=time.time()
#print(end)


a.start()
b.start()

a.join()
b.join()        



#for checking how much time taken to run

'''
import time
start=time.time

def fun1():
    for i in range(50):
        print(i)

fun1()
end=time.time()
print(end)'''

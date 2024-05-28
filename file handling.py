'''
a=open("C:/Users/New/Desktop/db_pro/irf.txt","r")
b=a.read()
print(b)
a.close()  '''


'''
a=open("C:/Users/New/Desktop/db_pro/irf.txt","r")
b=a.read()
print(len(b))
a.close()   '''


'''
a=open("C:/Users/New/Desktop/db_pro/irf.txt","r")
b=a.readlines()
print(len(b))
#print(b[:4])
print(b[2:7])
a.close()    '''


'''
a=open("C:/Users/New/Desktop/db_pro/irf.txt","a")
a.write("i am still learninggg pythonn")
a.close()
b=open("C:/Users/New/Desktop/db_pro/irf.txt","r")
print(b.read())
b.close()   '''





a=open("C:/Users/New/Desktop/db_pro/irf.txt","r")
a.close()
b=open("C:/Users/New/Desktop/db_pro/irf.txt","a")
b.write("i am a breakup guyyyyyyy")
b.close()
c=open("C:/Users/New/Desktop/db_pro/irf.txt","r")
print(c.read())
c.close()


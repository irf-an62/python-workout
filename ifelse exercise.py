'''
a=int(input("english:"))
b=int(input("tamil:"))
c=int(input("maths:"))
d=int(input("science:"))
e=int(input("social:"))
f=(a+b+c+d+e)/5
if(f<35):
    print("additional class is required:")
else:
    print("you are good to go")   '''





# task-1 (atm pin:)
'''
print("Enter your card")
pin=int(input("ENTER YOUR PIN:"))

if pin==2468:
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Banking")
    select=(input("select the option:"))
    if select=="1":
        a=int(input("Enter the amount:"))
        if a>=5000:
            print("Collect your amount")
        else:
            print("print valid amount")
    elif select=="2":
          c=int(input("Enter the deposit amount:"))
          if c>=1000:
             print("insert the amount")
          else:
             print("Enter the limit amount")
    elif select=="3":
             print("your balance is 10000")
else:
    print("Invalid pin")  '''
        
                        

#num1,num2,num3=int(input()),int(input()),int(input())

'''
num1, num2, num3 = int(input()), int(input()), int(input())
largest = max(num1, num2, num3)
sec = max(min(num1, num2), min(num1, num3), min(num2, num3))
third = min(num1, num2, num3)
print("largest no is", largest)
print("sec no is", sec)
print("third no is", third)  '''



'''up and down are same prgm

num1, num2, num3 = int(input()), int(input()), int(input())

largest = num1
sec = num2
third = num3

if num2 > largest:
    largest, sec = num2, largest
if num3 > largest:
    largest, sec, third = num3, largest, sec
elif num3 > sec:
    sec, third = num3, sec
elif num2 > sec:
    sec, third = num2, num1

print("largest no is", largest)
print("sec no is", sec)
print("third no is", third) '''



'''
num=10000000000000
print(f"{num:,d}")'''


#atm task (excption is used//)

'''
print("Enter your card")

while True: 
    try:
        pin = int(input("ENTER YOUR PIN:"))

        if pin == 2468:
            print("1.Withdraw")
            print("2.Deposit")
            print("3.Banking")
            select = input("select the option:")

            if select == "1":
                amount = int(input("Enter the amount:"))
                if amount >= 5000:
                    print("Collect your amount")
                else:
                    raise ValueError("Invalid amount")

            elif select == "2":
                deposit_amount = int(input("Enter the deposit amount:"))
                if deposit_amount >= 1000:
                    print("Insert the amount")
                else:
                    raise ValueError("Invalid deposit amount")

            elif select == "3":
                print("Your balance is 10000")
            break

        else:
            raise ValueError("Invalid PIN")

    except ValueError as ve:
        print(f"Error: {ve}")    '''



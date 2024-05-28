'''variables 

MyVarName=20
print(MyVarName)
                 '''


'''
(class variables)

class phone:
    chargertype="C-TYPE"
    
    def __init__(self,brand,price,processor):
        self.brand=brand
        self.price=price
        self.processor=processor
        
    def display(self):
         print("brand:",self.brand)
         print("price",self.price)
         print("processor",self.processor)
         print("chargertype",self.chargertype)

#(if v use this automatically it will change all chargetype, to b-type)
         #phone.chargertype="B-TYPE"


iphone=phone("iphone","1000000","i7")
iphone.display()

samsung=phone("samsung","100000","i5")
samsung.display()

oneplus=phone("one plus","10000","i3")
oneplus.display()
                  '''


'''class methods(multi level inheritance)


class grandpa():
    def phone(self):
        print("grandpa phone")

class dad(grandpa):
    def money(self):
        print("dads money")

class son(dad):
    def tab(self):
        print("sons tab")


irfan=son()
irfan.phone()
irfan.money()
irfan.tab()

nooh=dad()
nooh.phone()  '''


'''hierachy inheritance
class dad():
    def money(self):
        print("dad money")


class son2(dad):
    pass

class son2(dad):
    pass

class son2(dad):
    pass


s2=son2()
s2.money()
                  '''



'''hybrid inheritance


class dad():
    def money(self):
        print("dad money")

class land():
    def important(self):
        print("important land")
        
class son2(dad,land):
    pass

class son2(dad):
    pass

class son2(dad):
    pass


s2=son2()
s2.money()     '''

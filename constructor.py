class q:
    def __init__(self):
        print('constructor')

    def fun1(self):
        self.x=10
    def fun2(self):
        print('self.x')

obj=q()
obj.fun2()




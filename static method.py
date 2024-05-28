class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

     def detail(self):
         print("name:",self.name,"age:",self.age)

     @staticmethod
     def welcome():
         print("welcome to my page")
         


s1=student("irfan",22)
s1.detail()
s1.welcome

class father:
    def fishing(self):
        print("fishing in rivers")

    def chess(self):
        print("pl aying chess from mother")    
        

class mother:
    def fishing(self):
        print("fishing in rivers")

    def chess(self):
        print("playing chess from father")   


class son(father,mother):
    def riding(self):
        print("safe ride")


 
o=son()
o.riding()
o.fishing()
o.chess()

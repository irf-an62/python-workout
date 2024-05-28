#oru lib la book erkk,display panrom,borrow panrom,return panrommm:::::::::

class library:
    def __init__(self,books):
        self.books=books

    def listbooks(self):
        for book in self.books:
            print(book)


    def borrowbooks(self,borrowbooks):
        if borrowbooks in self.books:
            print("get your book now")
            self.books.remove(borrowbooks)

        else:
            print("book not availble")

    def receivebooks(self,receivebooks):
        print("you have returned a book")
        self.books.append(receivebooks)


books=["c++","c","python","java"]
o=library(books)

msg="""
    1.dispaly book
    2.borrow book
    3.return book
"""
while True:
    print(msg)
    ch=int(input("enter your choice:"))
    if ch==1:
        o.listbooks()
    elif ch==2:
        book=input("enter book name to borrow:")
        o.borrowbooks(book)
    elif ch==3:
        book=input("enter book name to return:")
        o.receivebooks(book)
    else:
        print("thank you come again")
        quit()     
        
        

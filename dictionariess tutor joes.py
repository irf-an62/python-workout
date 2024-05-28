a={
    "name":"irfan",
     "age":25,
     "ismarried":True
    }
print(a)
print(type(a))
print(a["age"])
print(a.get("age"))
print(a.keys())
print(a.values())
print(a.items())


for x in a:
    print(x)

for x in a:
    print(x,a[x])

for x in a.keys():
    print(x)
for x,y in a.items():
    print(x,y)


    

#changing values


a.update({"gender":"male"})
print(a)


#nested dictionaries

a={
    "a1":{
        "name":"irfan",
         "age":25,
         "ismarried":True
    },
    "a2":{
        "name":"irfan",
         "age":25,
         "ismarried":True
    }
    }
print(a)

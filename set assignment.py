unique={'apple','orange','banana','cherry','guava'}
print(unique)

##  5 unique integers
integers={1,2,3,4,5}
print(integers)

colors=["white","black","red","brown","blue","violet","green","yellow"]
sets=set(colors)
print(sets)

str="orange"
a=set(str)
print(a)

colors={"white","black","red","brown","blue","green"}
fruits={"apple","banana","orange","mango","cherry"}
joining=colors.union(fruits)
print(joining)

colors={"white","black","red","brown","blue","green", "orange"}
fruits={"apple","banana","orange","mango","cherry"}
inter=colors.intersection(fruits)
print(inter)

colors={"white","black","red","brown","blue","green"}
fruits={"apple","banana","orange","mango","cherry"}
print(colors.difference(fruits))
print(fruits.difference(colors))

colors={"white","black","red","brown","blue","green"}
fruits={"apple","banana","orange","mango","cherry"}
print(colors.symmetric_difference(fruits))
print(fruits.symmetric_difference(colors))

colors={"white","black","red","brown","blue","green"}
length=len(colors)
print(length)

colors={"white","black","red","brown","blue","green"}
print("orange" in colors)
print("red" in colors)

colors=["white","black","red","brown","blue","green"]
a=colors[1::2]
print(set(a))

colors={"white","black","red","brown","blue","green"}
removed=colors.pop()
print(removed)

colors={"white","black","red","brown","blue","green"}
colors.clear()
print(colors)

colors={"white","black","red","brown","blue","green"}
fruits={"apple","banana","orange","mango","cherry"}
print(len(colors)<len(fruits))

colors={"white","black","red","brown","blue","green"}

print(colors.isdisjoint(fruits))

a={1,2,3,4,5,6}
b={0,2,4,6,8}
print(a.isdisjoint(b))

colors=["white","black","red","brown","blue","green","red","brown"]
print(set(colors))

colors=("white","black","red","brown","blue","green")
print(set(colors))

colors={"white","black","red","brown","blue","green"}
fruits={"apple","banana","orange","mango","cherry"}
colors.update(fruits)
print(colors)

colors={"white","black","red","brown","blue","green"}
colors.update(["mango"])
print(colors)

colors={"white","black","red","brown","blue","green"}
colors.add("olive")
print(colors)

print(set(range(1,11)))

##set comprehension
## i dont know
#Tuple (immutable) function
a=("apple","banana","cherry","donat")
print(a)                    #print the tuple
print(len(a))               #The length of the tuple
print(len(a[2]))            #The length of the index value 2 in the tuple

#Find the type
print(type(a))

#Access the value using index
a=("apple","banana","cherry","donat")
print(a[2])         #access using postive indexing
print(a[-1])        #access using negative indexing
print(a[len(a)-1])  #access using the index with the help of len function

#Slicing the index
a=("apple","banana","cherry","donat")
print(a[1:3])           #slicing the tuple from 1 and 2
print(a[0:4])           #print all the value in the tuple
print(a[-4:])           #negative slicing

#slicing with step value
print(a[-1::-1])        #step value -1(backward passing)
print(a[1::2])          #strating from the index value 1 and print the step value
print(a[::-2])          #step value -2(backward passing)

#converting tuple to list & list to tuple
a=("apple","banana","cherry","donat")
b=list(a)                   #converting to tuple to list
b.pop(1)                    #removing the second element
print(b)                    #printing the b as list
b.remove("apple")           #removing the apple from the list
b.append("orange")          #adding orange to last list
b.insert(-1,"guava")#adding guava to the index value -1
c=tuple(b)                  #converting list into tuple
print(c)                    #printing to the tuple c

#cheching the item in the tuple
a=("apple","banana","cherry","orange","guava")
print("apple" in a)
print("banana" in a)
print("mango" in a)

#join the tuple using "+" operator
a=("apple","banana","cherry","orange", "mango")
b=(1,2,3,4,5,6)
c=(True, False)
print(a+b+c)
d=a+b+c
print(d)

#Deleting the tuple with del function
a=("apple","banana","cherry","orange", "mango")
# del a
# print(a)

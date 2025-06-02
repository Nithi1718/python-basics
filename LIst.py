#Type the list
a=["apple","banana","cherry","mango","lemon","orange"]
print(a)                                                    #print the list
print("length of the list: ", len(a))                       #length of the list
#print the item using indexing and negative indexing
print("first item in the list: " ,a[0])
print("last item in the list: " ,a[-1])
print("last item using the length -1", a[len(a)-1])         #len(a)-1
print(a[len(a)-2])                                          #len(a)-2 print the last before item in the list

#slicing th list
b=["apple","banana","cherry","mango","lemon","guava"]
print(len(b))
print(b[0:])                             #print all the items in the list
print(b[1:5])                            #print the items from 1 to 4
print(b[-6:])                            #print all the values using the negative indexing
print(b[-5:-2])                          #print the values from -5 to -3

# slicing with step value
print(b[::-1])                             #reverse printing all items
print(b[2::2])                             #print from third value with step value of 2
print(b[-1::-2])                           #printing from the last value with the step value 2
print(b[::3])                              #forward passing with step value 3
print(b[::-3])                             #backward passing with step value 3

#modifing the item inside the list
print("original list:", b)
b[0]="Item 1"
print("modified list: ", b)                 #modified the first value as "Item 1"
last_item=len(b)-1
b[last_item]="Final fruit"                  #assign the value to the last item in the list
print(b)
b[-1]=("apple")                             #again assign the value to the last item
print(b)
b[2]="apple"                                #assign the value to the 3rd position in the list
print(b)

#checking the item in the lit
print("apple" in b)                     #True
print("orange" in b)                    #False

#append "adding the item to the list"
b.append("lime")                  #add the value at the end of the list
b.append("orange")                #add item to the end of the list
print(b)

#inserting the item with indexing
a.insert(1,"apple")
print(a)
a.insert(0,"orange")          #value to the last item
print(a)

# Remove the items using pop method
animals=["dog","cat","deer","cow","snake","lion","tiger","zebra"]
animals.pop()                                   #The simple pop will remove the last item of the list
print(animals)
animals.pop(1)                                  #The pop(2) will remove the index 2 item
print(animals)

#Remove using the delete(del) function
del animals[2]          #Remove the mentioned index
print(animals)
del animals[1::2]       #Remove the index 1 item and the step item of 2 in the list
print(animals)
del animals[-1::-2]       #Removing from the last with the step value 2
print(animals)
# del animals                 #This will totally delete the list and cause "not defined error"
# print(animals)

#Removing with clear
animals=["dog","cat","deer","cow","snake","lion","tiger","zebra"]
animals.clear()             #This is useful for removing all the items in the list
print(animals)

#Joining the list(we can join as many list using "+" operator
#We can join string, integer, boolean, dictionary and all data types
a=["apple","banana","cherry","mango","lemon","orange"]
b=[1,2,3,4,5,6]
c=[True, False, {"lion":"leopad","tiger":"horse"}]

print(a+b)                          #This join a and b

join_all=a+b+c                      #This join a+b+c
print(join_all)

#Counting the how many times it repeated in the list
animals=["dog","cat","deer","cow","snake","lion","cat","dog","cat","tiger","zebra"]
print(animals.count("dog"))             #Count the dogs in the list
count_cat=animals.count("cat")                #Count the cats in the list
print(count_cat)

#Reverse the list using reverse function
a.reverse()             #Reversing the list "a"
print(a)
b.reverse()               #Reversing the list "B"
print(b)

#Print the list using range
print(list(range(10)))          #range from 0 to 9
print(list(range(1,10)))        #range from 1 to 9
print(list(range(0,11,2)))      #range from 0 to 11 with step value 2
print(list(range(1,11,2)))      #range from 1 to 11 with step value 2
print(list(range(10,0,-1)))     #range from 10 to 1 with step value 2
print(list(range(10,2,-2)))     #range from 10 to 2 with step value 2

#Remove the items from the list
#Remove using remove
animals=["dog","cat","deer","cow","snake","lion","tiger","zebra"]
print(animals)
animals.remove("snake")                                 #snake is removed using remove function
print("The snake is removed", animals)
print()
animals.remove(input("Enter the name of the animal: ")) #The entered animal name is removed from the list
print(animals)
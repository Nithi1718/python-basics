colors=("red","green","white","black","blue")
third_color=colors[2]
print(third_color)

numbers=(1,2,3,4,5,6,7,8,9)
random=numbers[5]
print(random)
last_numbers=numbers[-1]
print(last_numbers)

food=("biriyani","rasam","curd","parota","fish")
items=food
print(items)

new_variable=colors+numbers
print(new_variable)

numbers=(1,2,3,4,5,6,7,8,9)
first_three=numbers[:3]
print(first_three)

##tuple to list
tpl=("white","black","green","blue","violet","orange","pink")
lst=list(tpl)
print(lst)

negative=(-9,-8,-7,-6,-5,-4,-3,-2,-1)
zero=(0)            #we cant add single zero(0) to the in the tuple

#Either we can add two or more zeros in the tuple (0,0,0,0)

natural=(1,2,3,4,5,6,7,8,9)
real_numbers=negative+natural
print(tuple(real_numbers))


w=[-9,-8,-7,-6,-5,-4,-3,-2,-1]
z=[0]                     #Here we can add zeros in the list not in the tuple
n=[1,2,3,4,5,6,7,8,9]
print(w+z+n)

variable=(1,2,1,1,2,3,4,5,6,1,2,3)
##assign it to the multiplication
### doubt


colors=("red","white","blue","green","brown","yellow","black","pink","sandal")
print(len(colors))
mid_value=colors[4]
print(mid_value)

single_value=(1)
print(single_value)

numbers=(1,2,3,4,5,6,7,8,9)
colors=("red","green","white","black","blue")
print(numbers+colors)

numbers=(1,2,3,4,5,6,7,8,9)
print(max(numbers))

variable="concentration"
print(tuple(variable))
second_item=variable[1::2]
print(second_item)

tpl=()
print(tpl)

tuple1=(1,2,3,4,5,6,7,8,9)
tuple2=("red","green","white","black","blue")
tuple3=(tuple1+tuple2)
print(tuple3)

colors=("red","white","black","blue")
print("red" in colors)
print("ash" in colors)
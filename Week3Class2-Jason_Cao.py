my_num = [2, 4 ,6 ,8 ,10]

print("this is my orginal list:",my_num)

# updating the list 

#my_num[3] = 12

''''
#checking if this works: 
print("updated list:")
print(my_num)
print(my_num[3])
'''''

#adding more elements
'''
print("adding more elements") 
'''
my_num.append(12)
my_num.append(14)
my_num.append(16)

'''

print("this is my updated list:", my_num)

'''
# pop(i)

my_num.pop(2)
print("after using pop(i), my list is:", my_num)
my_num.pop()
print("after using pop(),my list is now:,", my_num)

# using the remove() function

my_num.remove(10)
print("after using the remove fuction we get:", my_num)

number = [1,4,7,9,2,8,10]

print("this is the orginal list:", number)

#min

print("the mininum # is:", min(number))

# max 

print("the maximum # is:", max(number))

#sum

print("the sum of all # is:", sum(number))

#dictionary

fruit = {
    "orange": 10, 
    "apples": 8, 
    "Banana": 5


}

print("updating the amount of oranges")

fruit["orange"] = 15 

print(fruit)

print("adding more fruits: ")

fruit['kiwi'] = 4 

print(fruit)

print("deleting apples")

del fruit["apples"]
print(fruit)
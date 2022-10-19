'''
@author: Devangini Patel

https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks
'''

# create a empty stack
print("task 1")
print("---------")
stack = []
arr = [1, 2, 3, 4]
print("stack", stack)

# add items to the stack
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)

print("")
print("task 2")
print("---------")
# Use a for loop to append the stack
for i in arr:
    stack.append(i)

print("stack", stack)

# pop all the items out
# while len(stack) > 0:
#     item = stack.pop()
#     print(item)

print("")
print("task 3")
print("---------")
# convert while to for
for i in stack:
    item = stack.pop()
print(item)

print("stack", stack)

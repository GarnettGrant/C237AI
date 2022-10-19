'''
@author: Devangini Patel

Reference: https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues
'''

# This script experiments with python queue data structure


from collections import deque

arr1 = []

queue = deque([])

print(queue)

queue.append("1")
queue.append("2")
queue.append("3")
queue.append("4")

print(queue)

while len(queue) > 0:
    item = queue.popleft()
    print(item)

print(queue)
print("garnett")
# Build a queue using single array
arr_queue = []

x = int(input("Enter a size for the array: "))
# Fill it using a for loop,
for i in x:
    arr_queue.append(i)

# Print the content using another loop
for i in arr_queue:
    print(i)

#1. Average

noplants = int(input("enter no of plants"))

hghts = [int(x) for x in input("enter heights: ").split()]

print("avg:",sum(hghts)/noplants)


#2.

# Python code to demonstrate Implementing
# stack using list
stack = [2, 3, 4]
stack.append("chandu")
stack.append("6")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack[-1])

# Python code to demonstrate Implementing
# Queue using deque and list
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)


#3.

str2 = 'Www.HackerRank.com'

print(str2.swapcase())


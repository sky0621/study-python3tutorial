stack = [3, 4, 5]
print(stack)
stack.append(6)
print(stack)
stack.pop()
stack.pop()
print(stack)

print("-------------------")

from collections import deque
q = deque(["Taro", "Jiro", "Saburo"])
print(q)
q.append("Siro")
print(q)
q.append("Goro")
print(q.popleft())
print(q)
print(q.popleft())
print(q)
print(q.popleft())
print(q)

print("-------------------")

squares = list()
print(squares)
squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = []
print(squares)
squares = [x**2 for x in range(10)]
print(squares)
#print(x)

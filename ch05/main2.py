# tuple is immutable
t = 123, 456, (789, '十', '二十')
print(t)
print(t[2])
print(t[2][1])

print("=================")

empty = ()
print(empty)
singleton = ('hello',) # listにするには末尾カンマが必要
print(singleton)

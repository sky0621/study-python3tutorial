print("# # # # # # # # # # # # # # # # # # # #")
print("listのループ")
print("# # # # # # # # # # # # # # # # # # # #")

words = ['dog', 'cat', 'mouse', 'rabbit', 'horse']
for w in words:
    print(w, len(w))

for w2 in words[:]:
    words.insert(0, w2)

print(words)

print(" ")
print("# # # # # # # # # # # # # # # # # # # #")
print("range")
print("# # # # # # # # # # # # # # # # # # # #")

for i in range(5):
    print(i)

print(" ")

for j in range(5, 10):
    print(j)

print(" ")

for k in range(0, 10, 3):
    print(k)

print(" ")
print("# # # # # # # # # # # # # # # # # # # #")
print("iterable")
print("# # # # # # # # # # # # # # # # # # # #")

print(list(range(5)))

print(" ")
print("# # # # # # # # # # # # # # # # # # # #")
print("for-else")
print("# # # # # # # # # # # # # # # # # # # #")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

print(list(range(10)))

print(range(10))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')

def culc(x, y):
    return lambda x, y: x * y

print(culc(5, 8))
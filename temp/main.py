def fib(n):
    a,b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

def xyz(x = 3, y = 4, z = 5):
    print(x + y + z)

xyz()
xyz(x = 5)
xyz(9, 2)
# xyz(1, 9, y = 10)

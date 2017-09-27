if __name__ == "__main__":
    i = 5

    def f(arg=i):
        print(arg)

    i = 6

    f()

    print()

    def fn(a, L=[]):
        L.append(a)
        return L

    print(fn(1))
    print(fn(2))
    print(fn(3))

    print()

    def fnn(a, L=None):
        if L == None:
            L = []
        L.append(a)
        return L

    print(fnn(1))
    print(fnn(2))
    print(fnn(3))

    l = list(range(3, 6))
    print()
    print(l)

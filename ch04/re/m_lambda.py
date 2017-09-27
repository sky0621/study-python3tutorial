if __name__ == "__main__":
    def make_incrementor(n):
        return lambda x: x + n

    f = make_incrementor(10)
    print(f(5))

    f2 = make_incrementor(99)
    print(f2(0))
    print(f2(1))

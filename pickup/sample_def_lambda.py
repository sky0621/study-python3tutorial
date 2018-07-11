print("# # # # # # # # # # # # # # # # # # # #")
print("ラムダ")
print("# # # # # # # # # # # # # # # # # # # #")

def func_multiple(n):
    return lambda x: x * n

multi3 = func_multiple(3)

print(multi3(5))
print(multi3(90))

print("")

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])
print(pairs)
pairs.sort(key=lambda p: p[0])
print(pairs)

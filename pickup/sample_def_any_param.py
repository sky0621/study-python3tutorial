print("# # # # # # # # # # # # # # # # # # # #")
print("任意の引数リスト")
print("# # # # # # # # # # # # # # # # # # # #")

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("a","b","c","d","e"))
print(concat("1","2","3","4", sep="-"))
print(concat("P", "y", "t", "h", "o", "n", "3", sep=""))

print("")
print("# # # # # # # # # # # # # # # # # # # #")
print("引数リストのアンパック")
print("# # # # # # # # # # # # # # # # # # # #")

print(list(range(3, 6)))
arg = [3, 6]
print(list(range(*arg)))
print("")

def language(php, python='2.7', golang='1.7.5'):
    print("golang:", golang)
    print("php", php)
    print("python", python)

d = {"php": "7", "python": "3.6.3", "golang": "1.9"}
language(**d)

print("")
d2 = {"php": "7"}
language(**d2)

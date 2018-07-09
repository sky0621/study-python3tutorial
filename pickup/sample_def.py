print("# # # # # # # # # # # # # # # # # # # #")
print("フィボナッチ")
print("# # # # # # # # # # # # # # # # # # # #")

def fib(n):
    """ n までのフィボナッチ級数を表示する """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

print(" ")

def fib2(n):
    """ n までのフィボナッチ級数を表示する """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

res = fib2(2000)
print(res)

print(" ")
print("# # # # # # # # # # # # # # # # # # # #")
print("デフォルト引数")
print("【注意】デフォルト値は一度だけ初期化されるため、可変オブジェクトをデフォルト引数にすると、コールのたびにデフォルト値が変わっていく。")
print("# # # # # # # # # # # # # # # # # # # #")

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print(" ")

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2))
print(f2(3))

print(" ")
print("# # # # # # # # # # # # # # # # # # # #")
print("キーワード引数")
print("# # # # # # # # # # # # # # # # # # # #")

print("引数１個、オプション引数３個の parrot 関数を定義")
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

print(" ")
print(" > 位置引数１個")
parrot(1000)

print(" ")
print(" > キーワード引数１個")
parrot(voltage=2000)

print(" ")
print(" > キーワード引数2個")
parrot(voltage=3000, action='VOOOOOOM')

print(" ")
print(" > キーワード引数2個(入れ替え)")
parrot(action='VoooooooooooooooooooM', voltage=4000)

print(" ")
print(" > 位置引数3個")
parrot('a million', 'bereft of life', 'jump')

print(" ")
print(" > 位置引数１個、キーワード引数3個")
parrot(6000, state='stesteste', action='vo', type='Wine Red')


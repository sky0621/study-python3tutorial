x = int(input("整数を入れてください："))

if x < 0:
    x = 0
    print("負数は０とする")
elif x == 0:
    print("ゼロ")
elif x == 1:
    print("ひとつ")
else:
    print("もっと")

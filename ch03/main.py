print(2+2)

print("""
    This is a pen.
    That is a pencil.
""")

a, b = 0, 1
while b < 50:
    print(b, end=',')
    a, b = b, a+b

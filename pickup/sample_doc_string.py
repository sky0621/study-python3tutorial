print("# # # # # # # # # # # # # # # # # # # #")
print("ドキュメンテーション文字列")
print("# # # # # # # # # # # # # # # # # # # #")

def myfunc():
    """ Explain myfunc

    other explain.
    """
    pass

print(myfunc.__doc__)
print("")
print("")

def myfunc2():
    """Explain myfunc

other explain.
other explain2.
"""
    pass

print(myfunc2.__doc__)

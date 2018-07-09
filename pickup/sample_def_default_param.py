print("# # # # # # # # # # # # # # # # # # # #")
print("デフォルト引数")
print("# # # # # # # # # # # # # # # # # # # #")

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'Y', 'yes', 'Yes'):
            print('got yes')
            return True
        if ok in ('n', 'N', 'no', 'No'):
            print('got no')
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('非協力的ユーザー')
        print(complaint)

# ask_ok()
# TypeError: ask_ok() missing 1 required positional argument: 'prompt'

ask_ok('Do you really want to quit?', 2, 'Come on, only yes or no!')

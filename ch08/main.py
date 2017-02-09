import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS Error: {0}".format(err))
except ValueError:
    print("データが整数に変換できません。")
except:
    print("予期せぬエラー： ", sys.exc_info()[0])
    raise


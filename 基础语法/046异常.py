try:
    f = open('aaaa.txt','r')
    print(f.read())
except FileNotFoundError:
    print("没有文件")
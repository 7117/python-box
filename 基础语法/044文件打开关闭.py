# 文件的创建
f = open('044文件打开关闭.log', 'w')
f.close()


# 文件的读写
f = open('044文件打开关闭.log', 'w')
f.write('hello,hello')
f.close()


# 文件的读取
f = open('044文件打开关闭.log', 'r')
content = f.read(5)
print(content)
f.close()

# 文件的读取
f = open('044文件打开关闭.log', 'r')
content = f.readline()
print(content)

# 读取文章
f = open('044文件打开关闭.log', 'r')
content = f.readlines()
print(type(content))
print(content)
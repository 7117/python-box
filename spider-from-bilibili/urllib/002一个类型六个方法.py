import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
print(type(response))

# 读取两个字符
print(response.read(2))

# 读取一行
print(response.readline())

# 获取状态码
print(response.getcode())

# 获取URl
print(response.geturl())

# 获取是一个状态信息
print(response.getheaders())

# # 读取多行
# print(response.readlines())

# 一个类型 HTTPResponse
# 六个方法 read  readline  readlines  getcode geturl getheaders


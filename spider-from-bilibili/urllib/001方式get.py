import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# （3）获取响应中的页面的源码  content 内容的意思
# read方法  返回的是字节形式的二进制数据
# 我们要将二进制的数据转换为字符串
# 二进制--》字符串  解码  decode('编码的格式')
content = response.read().decode('utf-8')
f = open('001方式get.html', 'w')
f.write(content)
f.close()
print(content)






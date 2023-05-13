import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求的参数 是不会拼接在url的后面的  而是需要放在请求对象定制的参数中
# post请求的参数 必须要进行编码
# 多个data就表明是post请求了
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')
# print(content)


# 字符串--》json对象
obj = json.loads(content)
print(obj)

# post请求方式的参数 必须编码   data = urllib.parse.urlencode(data)
# 编码之后 必须调用encode方法 data = urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求对象定制的方法中  request = urllib.request.Request(url=url,data=data,headers=headers)
# var = {'errno': 0, 'data': [{'k': 'spider', 'v': 'n. 蜘蛛; 星形轮，十字叉; 带柄三脚平底锅; 三脚架'},
#                             {'k': 'Spider', 'v': '[电影]蜘蛛'},
#                             {'k': 'SPIDER', 'v': 'abbr. SEMATECH process induced damage effect revea'},
#                             {'k': 'spiders', 'v': 'n. 蜘蛛( spider的名词复数 )'},
#                             {'k': 'spidery', 'v': 'adj. 像蜘蛛腿一般细长的; 象蜘蛛网的，十分精致的'}]}
#

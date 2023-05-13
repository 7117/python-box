# urlencode应用场景：多个参数的时候
# https://www.baidu.com/s?wd=周杰伦&sex=男

import urllib.parse

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

a = urllib.parse.urlencode(data)
print(a)
# wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81

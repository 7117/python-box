import urllib.request
import urllib.error

url = 'https://www,baidu111.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

try:
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(f'正确的{content}')
except urllib.error.HTTPError:
    print("系统正在升级")
except urllib.error.URLError:
    print("url错误")

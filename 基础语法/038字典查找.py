info = {'name':'sunxiao','age':19}
print(info)
# 不存在会返回错误
# get方式不存在会返回none
print(info['name'])
print(info.get('name'))
print(info.get('namea','sunlei'))


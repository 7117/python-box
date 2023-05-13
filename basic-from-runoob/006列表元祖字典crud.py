# 增加
fool_list = ['a', 'b', 'c']
print(fool_list)

fool_list.append('d')
print(fool_list)

fool_list.insert(1, 'insert')
print(fool_list)

num_list = [1, 2, 3]
num1_list = [4, 5, 6]
num_list.extend(num1_list)
print(num_list)

# 修改
city_list = ['a', 'b', 'c']
city_list[1] = 'gg'
print(city_list)

# 删除
city_list = ['a', 'b', 'c', 'd', 'e', 'f']
del city_list[0]
print(city_list)
city_list.remove('c')
print(city_list)
print("pop", city_list)
city_list.pop()
print("pop", city_list)

# ============================================================
a_tuple = (1, 2, 3, 4, 5, 6)

print(a_tuple)
print(a_tuple[1])

# 元祖不可以修改里面的内容
# a_tuple[2] = 3
# print(a_tuple)

print(a_tuple)

b_tuple = (3)
print(b_tuple)

# ============================================================
info = {'name': 'sunxiao', 'age': 19}
print(info)
# 不存在会返回错误
# get方式不存在会返回none
print(info['name'])
print(info.get('name'))
print(info.get('namea', 'sunlei'))
info = {'name': 'sunxiao', 'age': 19}
print(info)
info['name'] = 'sunlei'
print(info)

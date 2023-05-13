name = "a"
age = 22
print('我的名字是 %s,我的年龄是%d' % (name, age))

# a = input('请输入您的密码')
# print('我的密码是%s' % a)

f = open("support\doo.txt", "w")
f.write("ssssqqqqqq\nssssssssssss")
f.close()

r = open("support\doo.txt", "r")
str = r.read()
print(2, str)

re = open("support\doo.txt", "r")
strs = re.readline()
print(3, strs)

ref = open("support\doo.txt", "rb+")
refs = ref.seek(3)
print(4, ref.read(1))

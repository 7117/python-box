def printName(strs):
    print(strs)
    return


printName("printName")


# 默认参数
def printinfo(name, age=35):
    print("Name: ", name, "Age ", age)
    return


printinfo(age=50, name="miki")
printinfo(name="miki")


# 不定长参数
def printinfo(arg1, *vartuple):
    print("输出:", arg1)
    for var in vartuple:
        print("我是内部：", var)
    return


printinfo(10)
printinfo(70, 60, 50)

sum = lambda arg1, arg2: arg1 + arg2
print("lambda相加后的值为 : ", sum(10, 20))


def sumPlus(arg1, arg2):
    total = arg1 + arg2
    return total


print("sum相加的值：", sumPlus(10, 20))

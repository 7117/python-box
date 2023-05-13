def print_func_out(par):
    print("我是内部的",__name__)
    print(par)
if __name__ == '__main__':
    print('程序自身在运行')
else:
    def print_func_in(par):
        print(par)
        return
    print('我来自另一模块')

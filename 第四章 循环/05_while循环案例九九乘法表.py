"""
演示while的嵌套循环
打印输出九九乘法表
"""
# 定义外层循环的控制变量
x = 1
while x < 10:
    # 定义内层循环的控制变量
    y = 1
    while y <= x:
        print(f"{y} ✖ {x} = {x*y}\t",end="")
        y += 1
    x += 1
    print() #换行作用
"""
演示for循环打印九九乘法表
"""
# 通过外层循环控制行数
for x in range(1, 10):
    # 通过内存循环控制每一行的数据
    for y in range(1, x + 1):
        print(f"{y} * {x} = {x * y}\t", end="")
    # 外层循环可以通过print输出一个回车符
    print()

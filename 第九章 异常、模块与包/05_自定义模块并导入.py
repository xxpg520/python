"""
演示自定义模块

注意事项:不同模块, 同名的功能, 如果都被导入,那么后倒入的会覆盖先导入的
"""

# 导入自定义模块使用
# 方法1:
# import my_module1
# my_module1.test(1, 2)

# 方法2:
# from my_module1 import test
# test(1, 2)

# 导入不同模块的同名功能
# from my_module1 import test
# from my_module2 import test
# test(1, 2)

# __main__变量
# from my_module1 import test

# __all__变量 用来控制列表中被导入的内容
from my_module1 import *
test_a(1, 2)
test_b(1, 2)

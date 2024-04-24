"""
演示函数作为参数传递
1. 函数本身可以作为参数, 传入另一个函数中进行使用
2. 将函数传入的作用在于: 传入计算逻辑,而非传入数据
"""

# 定义一个函数, 接收另一个函数作为传入参数
def test_func(compute):
    result = compute(1, 2) # 确定compute是函数
    print(f"compute参数的类型是:{type(compute)}")
    print(f"计算结果:{result}")

# 定义一个函数, 准备作为参数传入另一个函数
def compute(x, y):
    return x + y
# 调用, 并传入函数
test_func(compute)

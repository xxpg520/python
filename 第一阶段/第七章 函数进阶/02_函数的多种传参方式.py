"""
演示函数的多种传参方式
"""


def user_info(name, age, gender):
    print(f"姓名是: {name}, 年龄是: {age}, 性别是:{gender}")


# 位置参数 - 默认使用形式
user_info('小明', 20, '男')

# 关键字参数
user_info(name='小王', age=11, gender='女')
user_info(age=10, gender='女', name='潇潇')  # 可以不按照参数的定义顺序传参
user_info('甜甜',gender='女', age=9)

# 缺省参数(默认值)
def user_info(name, age, gender='男'): # 默认值的参数必须定义在最后
    print(f"姓名是: {name}, 年龄是: {age}, 性别是:{gender}")
user_info('小天', 13)
user_info('小天', 13, gender='女')

# 不定长参数(可变参数)
# 不定长 - 位置不定长, *号  作为元组存在
def user_info(*args):  # 规范args, 非必须
    print(f"args参数的类型是:{type(args)}, 内容是:{args}")
user_info(1, 2, 3, '小明', '男孩')

# 不定长 - 关键字不定长, **号  作为字典存在
def user_info(**kwargs):  # 规范args, 非必须
    print(f"args参数的类型是:{type(kwargs)}, 内容是:{kwargs}")
user_info(name='小王', age=11, gender='男孩')


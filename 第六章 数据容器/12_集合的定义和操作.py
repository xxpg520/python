"""
演示数据容器集合的使用
---集合不支持下表索引
---集合允许修改
"""

# 定义集合
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima",}
my_set_empty = set()
print(f"my_set的内容是：{my_set},类型是{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty},类型是{type(my_set_empty)}")
# 输出：my_set的内容是：{'传智教育', '黑马程序员', 'itheima'},类型是<class 'set'>
# 输出：my_set_empty的内容是：set(),类型是<class 'set'>


# 添加新元素
my_set.add("Python")
my_set.add("传智教育")
print(f"my_set添加元素后的结果是：{my_set}")
# 输出：my_set添加元素后的结果是：{'传智教育', '黑马程序员', 'itheima', 'Python'}

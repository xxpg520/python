"""
演示数据容器集合的使用
特点：
1、可以容纳多个数据
2、可以容纳不同类型的数据（混装）
3、数据是无序存储的（不支持下标索引）
4、不允许重复数据存在
5、可以修改（增加或删除元素等）
6、支持for循环
"""

# 定义集合
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima",}
my_set_empty = set()
print(f"my_set的内容是：{my_set},类型是{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty},类型是{type(my_set_empty)}")
# 输出：my_set的内容是：{'传智教育', '黑马程序员', 'itheima'},类型是<class 'set'>
# 输出：my_set_empty的内容是：set(),类型是<class 'set'>


# 添加新元素 集合.add()
my_set.add("Python")
my_set.add("传智教育")
print(f"my_set添加元素后的结果是：{my_set}")
# 输出：my_set添加元素后的结果是：{'传智教育', '黑马程序员', 'itheima', 'Python'}

# 移除元素  集合.remove()
my_set.remove("黑马程序员")
print(f"my_set移除黑马程序员后，结果是{my_set}")
# 输出：my_set移除黑马程序员后，结果是{'itheima', 'Python', '传智教育'}

# 随机取出元素  集合.pop()
my_set = {"传智教育", "黑马程序员", "itheima"}
element = my_set.pop()
print(f"集合被取出的元素是：{element}，取出元素后还剩：{my_set}")
# 输出：集合被取出的元素是：黑马程序员，取出元素后还剩：{'传智教育', 'itheima'}

# 清空集合 集合.clear()
my_set.clear()
print(f"使用clear清空结合后，my_set还剩：{my_set}")
# 结果：使用clear清空结合后，my_set还剩：set()

# 取2个集合的差集 集合1.difference(集合2)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"取出差集的结果是：{set3}")
print(f"取差集后，原有set1内容：{set1}")
print(f"取差集后，原有set2内容：{set2}")
# 结果：取出差集的结果是：{2, 3}
# 结果：取差集后，原有set1内容：{1, 2, 3}
# 结果：取差集后，原有set2内容：{1, 5, 6}

# 消除2个集合的差集   集合1.difference_update(集合2)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"消除差集后，集合set1结果：{set1}")
print(f"消除差集后，集合set2结果：{set2}")
# 结果：消除差集后，集合set1结果：{2, 3}
# 结果：消除差集后，集合set2结果：{1, 5, 6}

# 2个集合合并   集合1.union(集合2)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"用union合并后，set3结果：{set3}")
print(f"用union合并后，set1结果：{set1}")
print(f"用union合并后，set2结果：{set2}")
# 结果：用union合并后，set3结果：{1, 2, 3, 5, 6}
# 结果：用union合并后，set1结果：{1, 2, 3}
# 结果：用union合并后，set2结果：{1, 5, 6}

# 统计集合元素数量 len(集合）
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
num = len(set1)
print(f"集合内的元素数量有：{num}个")
# 结果：集合内的元素数量有：5个

# 集合的遍历
# 不支持下标索引，所以不能用while循环
# 可以用for循环
set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(f"集合的元素有：{element}")
# 结果：
# 集合的元素有1
# 集合的元素有2
# 集合的元素有3
# 集合的元素有4
# 集合的元素有5
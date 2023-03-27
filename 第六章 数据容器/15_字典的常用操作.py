"""
演示字典的常用操作
特点：
1、可以容纳多个数据
2、可以容纳不同类型的数据
3、每一份数据是Key Vlave键值对
4、可以通过Key获取到Value，Key不可重复（重复会覆盖）
5、不支持下标索引
6、可以修改（增加或删除更新元素等）
7、支持for循环，不支持while循环
"""

my_dict = {"周杰轮": 99, "林俊节": 88, "张学油": 77}
# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素，结果：{my_dict}")
# 字典经过新增元素，结果：{'周杰轮': 99, '林俊节': 88, '张学油': 77, '张信哲': 66}

# 更新元素   字典[key] = value值
my_dict["周杰轮"] = 33
print(f"字典经过更新后，结果是：{my_dict}")
# 字典经过更新后，结果是：{'周杰轮': 33, '林俊节': 88, '张学油': 77, '张信哲': 66}

# 删除元素    字典.pop(key)
score = my_dict.pop("周杰轮")
print(f"字典中被移除了一个元素，结果{my_dict}，周杰轮的考试分数是：{score}")
# 字典中被移除了一个元素，结果{'林俊节': 88, '张学油': 77, '张信哲': 66}，周杰轮的考试分数是：33

# 清空元素，clear   字典.clear()
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")
# 字典被清空了，内容是：{}

# 获取全部的key  字典.keys()
my_dict = {"周杰轮": 99, "林俊节": 88, "张学油": 77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")
# 字典的全部keys是：dict_keys(['周杰轮', '林俊节', '张学油'])

# 遍历字典
# 方式1：通过获取到全部的key来完成便利到4wr玩
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是：{my_dict[key]}")
# 字典的key是：周杰轮
# 字典的value是：99
# 字典的key是：林俊节
# 字典的value是：88
# 字典的key是：张学油
# 字典的value是：77

# 统计字典内的元素数量，len()函数   字典.len()
num = len(my_dict)
print(f"字典中的元素数量有：{num}个")
# 字典中的元素数量有：3个

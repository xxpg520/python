my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

# max最大元素
print(f"列表 最大的元素是：{max(my_list)}")
print(f"元组 最大的元素是：{max(my_tuple)}")
print(f"字符串最大的元素是：{max(my_str)}")
print(f"集合 最大的元素是：{max(my_set)}")
print(f"字典 最大的元素是：{max(my_dict)}")

# min最小元素
print(f"列表 最小的元素是：{min(my_list)}")
print(f"元组 最小的元素是：{min(my_tuple)}")
print(f"字符串最小的元素是：{min(my_str)}")
print(f"集合 最小的元素是：{min(my_set)}")
print(f"字典 最小的元素是：{min(my_dict)}")

# 类型转换: 容器转列表
print(f"列表转换列表的结果是：{list(my_list)}")
print(f"元组 转换列表的结果是：{list(my_tuple)}")
print(f"字符串转换列表的结果是：{list(my_str)}")
print(f"集合 转换列表的结果是：{list(my_set)}")
print(f"字典 转换列表的结果是：{list(my_dict)}")

# 类型转换: 容器转元组
print(f"列表 转换元组的结果是：{tuple(my_list)}")
print(f"元组 转换元组的结果是：{tuple(my_tuple)}")
print(f"字符串转换元组的结果是：{tuple(my_str)}")
print(f"集合 转换元组的结果是：{tuple(my_set)}")
print(f"字典 转换元组的结果是：{tuple(my_dict)}")

# 类型转换: 容器转元组
print(f"列表 转换字符串的结果是：{str(my_list)}")
print(f"元组 转换字符串的结果是：{str(my_tuple)}")
print(f"字符串转换字符串的结果是：{str(my_str)}")
print(f"集合 转换字符串的结果是：{str(my_set)}")
print(f"字典 转换字符串的结果是：{str(my_dict)}")

# 类型转换: 容器转集合
print(f"列表 转换集合的结果是：{set(my_list)}")
print(f"元组 转换集合的结果是：{set(my_tuple)}")
print(f"字符串转换集合的结果是：{set(my_str)}")
print(f"集合 转换集合的结果是：{set(my_set)}")
print(f"字典 转换集合的结果是：{set(my_dict)}")

# 进行容器的排序
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "bdcefga"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}

print(f"列表对象的排序结果: {sorted(my_list)}")
print(f"元组对象的排序结果: {sorted(my_tuple)}")
print(f"字符串对象的排序结果: {sorted(my_str)}")
print(f"集合对象的排序结果: {sorted(my_set)}")
print(f"字典对象的排序结果: {sorted(my_dict)}")

print(f"列表对象的反向排序结果: {sorted(my_list, reverse=True)}")
print(f"元组对象的反向排序结果: {sorted(my_tuple, reverse=True)}")
print(f"字符串对象反向的排序结果: {sorted(my_str, reverse=True)}")
print(f"集合对象的反向排序结果: {sorted(my_set, reverse=True)}")
print(f"字典对象的反向排序结果: {sorted(my_dict, reverse=True)}")
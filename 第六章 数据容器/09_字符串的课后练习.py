"""
字符串联系案例：分割字符串
"""
# 给定一个字符串：“itheima itcast boxuegu"
my_str = "itheima itcast boxuegu"
# 统计字符串内有多少个"it"字符
count = my_str.count("it")
print(f"字符串{my_str}中有：{count}个it字符")
# 将字符串内的空格，全部替换为字符串："|"
new_my_str = my_str.replace(" ", "|")
print(f"字符串{my_str},被替换空格后，结果是：{new_my_str}")
# 并按照"|"进行字符串分割，得到列表
new2_my_str = new_my_str.split("|")
print(f"字符串{new_my_str},按照|分割后，得到：{new2_my_str}")


"""
练习案例：数一数有几个a
"""
# 定义字符串变量name，内容为："itheima is a brand of itcast"
# 通过for循环，遍历此字符串，统计有多少英文字母："a"

name ="itheima is a brand of itcast"
count = 0
for num in name:
    if num == "a":
        count += 1
print(f"{name}中共含有：{count}个字母a")
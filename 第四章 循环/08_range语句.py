"""
range(num)语句
"""
# 语法1：
# range(num)
# 获取一个从0开始，到num结束的数字序列（不包含num本身）
for x in range(5):
    print(x)

# 语法2：
# range(num1, num2)
# 获得一个从num1开始，到num2结束的数字序列（不含num2本身）
for x in range(5, 10):
    print(x)

# 语法3：
# range(num1, num2, step)
# 获得一个从num1开始，到num2结束的数字序列（不包含num2本身）
# 数字之间的步长，以step为准（step默认为1）
for x in range(5, 10, 2):
    print(x)
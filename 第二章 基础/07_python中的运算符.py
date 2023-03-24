"""
演示Python中的各类运算符
"""
# 算数(数字)运算符
print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("3 * 3 = ", 3 * 3)
print("4 / 2 = ", 4 / 2)

# 求 整数
print("11 // 2 = ", 11 // 2)
# 求 余数
print("9 % 2 = ", 9 % 2)
# 求 指数
print("2 ** 2 = ", 2 ** 2)

# 赋值运算符
num = 1 + 2 + 3
# 复合复制运算符  +=
num = 1
# num = num + 1
num += 1
print("num += 1: ", num)

# num = num - 1
num -= 1
print("num -= 1: ", num)

# num = num * 4
num *= 4
print("num *= 4: ", num)

# num = num ÷ 2
num /= 2
print("num /= 2: ", int(num))

num = 3
# num = num除以2的余数
num %= 2
print("num %= 2: ", num)

# num = num的2次方
num **= 2
print("num **= 2: ", num)


num = 9
# num = num除以2的整数
num //= 2
print("num //= 2: ", num)

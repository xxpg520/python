"""
tuple 元组
特点是不能添加和删除，可以使用索引访问
"""
classmates = ('Michael', 'Bob', 'Tracy') # 定义一个元组
# 输出元组中序号为1的元素
print(classmates[1])

t = (1, 2)
print(t)

# 定义一个空tuple
t = ()
print(t)

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1, )
print(t)


# 可变的tuple，
t = ('a', 'b', ['A', 'B'])
# 只有元组中的列表是可以修改
t[2][0] = "X"
t[2][1] = "Y"
print(t)


# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'Php'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple：
print(L[0][0])
# 打印Python：
print(L[1][1])
# 打印Lisa:
print(L[2][2])
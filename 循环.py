"""
循环
"""
# for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 计算1-100的整数之和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while循环
# 计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(f"Hello, {x}!")

# break 退出循环
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print("END")


# continue跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue   # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
# """练习4-1：比萨
# 想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环
# 将每种比萨的名称打印出来。
# - 修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。
# 对于每种比萨，都显示一行输出，下面是一个例子。
#     I like pepperoni pizza
# - 在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。
# 输出应包含针对每种比萨的消息，还有一个总结性句子，下面是一个例子。
#     I really love pizza!
# """
# pizza_list = ["水果披萨", "芝士披萨", "火腿披萨"]
# for pizza in pizza_list:
#     print(f"我喜欢{pizza}")
# print("我真的很喜欢披萨")
"""

练习4-2：动物
想出至少三种有共同特征的动物，将其名称存储在一个列表中，再使用for 循环将每种动物的名称打印出来。
修改这个程序，使其针对每种动物都打印一个句子，下面是一个例子。
A dog would make a great pet.
在程序末尾添加一行代码，指出这些动物的共同之处，如打印下面这样的句子。
Any of these animals would make a great pet!
"""
# pet_list = ["dog", "cat", "hamster"]
# for pet in pet_list:
#     print(f"A {pet} would mak a great pet")
# print("Any of these animals would make a great pet!")

# 练习4-3：
# 数到20 使用一个for 循环打印数1～20（含）。
# for i in range(21):
#     print(i)

# """
# 练习4-4：一百万
# 创建一个包含数1～1 000 000的列表，再使
# 用一个for 循环将这些数打印出来。（如果输出的时间太长，
# 按Ctrl + C停止输出或关闭输出窗口。
# """
# numbers = []
# for num in range(1, 1000001):
#     numbers.append(num)
# for num in numbers:
#     print(num)

# """
# 练习4-5：一百万求和
# 创建一个包含数1～1 000 000的列
# 表，再使用min() 和max() 核实该列表确实是从1开始、到1
# 000 000结束的。另外，对这个列表调用函数sum() ，看看
# Python将一百万个数相加需要多长时间
# """
# list_number = list(range(1, 1000001))
# print(min(list_number))
# print(max(list_number))
# print(type(list_number))
# print(sum(list_number))
# sum_list_number = 0
# for number in list_number:
#     sum_list_number += number
# print(sum_list_number)

# """
# 练习4-6：奇数 通过给函数range() 指定第三个参数来创建
# 一个列表，其中包含1～20的奇数，再使用一个for 循环将这
# 些数打印出来
# """
# number_list = list(range(1, 21, 2))
# for lm in number_list:
#     print(lm)

# """
# 练习4-7：3的倍数 创建一个列表，其中包含3～30能被3整除
# 的数，再使用一个for 循环将这个列表中的数打印出来。
# """
# number2 = list(range(3, 31, 3))
# for nm in number2:
#     print(nm)

# """
# 练习4-8：立方 将同一个数乘三次称为立方 。例如，在
# Python中，2的立方用2**3 表示。请创建一个列表，其中包含
# 前10个整数（1～10）的立方，再使用一个for 循环将这些立
# 方数打印出来。
# """
# number3 = list(range(1,11))
# lf = 0
# for n3 in number3:
#     lf = n3**3
#     print(lf)

# """
# 练习4-9：立方解析 使用列表解析生成一个列表，其中包含
# 前10个整数的立方。
# """
# list_number2 = [i**3 for i in range(1, 11)]
# print(list_number2)

# """
# 练习4-10：切片
# 选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表的中间三个元素。
# 打印消息“The last three items in the list are:”，再使用切片来打印列表的末尾三个元素。
# """
# numbers = []
# for num in range(1, 1000001):
#     numbers.append(num)
# print(f"The first three items in the list are: {numbers[:3]}")
# print(f"Three items from the middle of the list are:{numbers[500000:500003]}")
# print(f"The last three items in the list are:{numbers[-3:]}")

# """
# 练习4-11：你的比萨，我的比萨
# 在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其赋给变量friend_pizzas ，再完成如下任务。
# 在原来的比萨列表中添加一种比萨。
# 在列表friend_pizzas 中添加另一种比萨。
# 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一
# 个列表；打印消息“My friend's favorite pizzas are:”，再使用一个for循环来打印第二个列表。核实
# 新增的比萨被添加到了正确的列表中
# """
# pizza_list = ["水果披萨", "芝士披萨", "火腿披萨"]
# friend_pizzas = pizza_list[:]
# friend_pizzas.append("奶油披萨")
# for pizzas in pizza_list:
#     print(f"我最喜欢的披萨是:{pizzas}")
# for pizzas in friend_pizzas:
#     print(f"我朋友最喜欢的披萨是:{pizzas}")

"""
练习4-12：使用多个循环 在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for 循环来打印列表。
请选择一个版本的foods.py，在其中编写两个for 循环，将各个食品列表打印出来。
"""
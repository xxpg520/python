"""
第三章 列表 练习
3-1 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
3-2 问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
3-4 嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。
"""
names = ['张无忌', '周芷若', '阳顶天', '谢逊']
food = "一起吃饭吧！"
print(food + names[0])
print(food + names[1])
print(food + names[2])
print(food + names[3])

# 3-5 修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
print(names[2] + '因为走火入魔不能来吃饭')
names[2] = '张三丰'
print(food + names[0])
print(food + names[1])
print(food + names[2])
print(food + names[3])

"""
3-6 添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
使用insert() 将一位新嘉宾添加到名单开头。
使用insert() 将另一位新嘉宾添加到名单中间。
使用append() 将最后一位新嘉宾添加到名单末尾。
打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
names.insert(0, '张翠山')
names.insert(3, '殷素素')
names.append('韦一笑')
print(f"{food}{names}")

"""
3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进
晚餐。
对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
"""
print("不好意思，因为疫情原因，不能大规模聚餐")
not_names = names.pop(0)
print(f"尊敬的：{not_names} ,无法邀请您来共进晚餐")
not_names = names.pop(1)
print(f"尊敬的：{not_names} ,无法邀请您来共进晚餐")
not_names = names.pop(1)
print(f"尊敬的：{not_names} ,无法邀请您来共进晚餐")
not_names = names.pop(1)
print(f"尊敬的：{not_names} ,无法邀请您来共进晚餐")
not_names = names.pop(2)
print(f"尊敬的：{not_names} ,无法邀请您来共进晚餐")
print(f"尊敬的：{names[0]}，您仍在晚宴邀请之列")
print(f"尊敬的：{names[1]}，您仍在晚宴邀请之列")

fruits = ['apple', 'banana', 'pear', 'litchi', 'mango']
fruits.insert(0, '')

"""
练习3-8：放眼世界 想出至少5个你渴望去旅游的地方。
将这些地方存储在一个列表中，并确保其中的元素不是按字母
顺序排列的。
按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，
只管打印原始Python列表练习
"""
scenic_spot = ['Hawaii', 'Iceland', 'Tokyo', 'London', 'Paris']
print(scenic_spot)
# 使用sorted() 按字母顺序打印这个列表，同时不要修改它。
print(sorted(scenic_spot))
# 再次打印该列表，核实排列顺序未变。
print(scenic_spot)
# 使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它
print(sorted(scenic_spot, reverse=True))
# 再次打印该列表，核实排列顺序未变
print(scenic_spot)
# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
scenic_spot.reverse()
print(scenic_spot)
# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
scenic_spot.reverse()
print(scenic_spot)
# 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
scenic_spot.sort()
print(scenic_spot)
# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了
scenic_spot.sort(reverse=True)
print(scenic_spot)

"""
练习3-9：晚餐嘉宾 在完成练习3-4~练习3-7时编写的程序之
一中，使用len() 打印一条消息，指出你邀请了多少位嘉宾来
共进晚餐。
"""
sum_names = len(names)
print(f"共邀请了:{sum_names}嘉宾")

"""
练习3-10：尝试使用各个函数 想想可存储到列表中的东
西，如山川、河流、国家、城市、语言或你喜欢的任何东西。
编写一个程序，在其中创建一个包含这些元素的列表，然后，
对于本章介绍的每个函数，都至少使用一次来处理这个列表。
"""
Fruits = ['Banana', 'Apple', 'Mango', 'litchi', 'strawberry']
print(Fruits)
Fruits.reverse()
print(Fruits)
Fruits.sort()
print(Fruits)
Fruits.sort(reverse=True)
print(Fruits)
Fruits_1 = Fruits.pop(1)
print(Fruits)
print(Fruits_1)
Fruits.insert(1, 'litchi')
print(Fruits)
del Fruits[0]
print(Fruits)
print(len(Fruits))

# # 超出索引范围示范
# f = []
# print(f[-1])

print(Fruits.index('Banana'))

even_numbers = list(range(21))
print(even_numbers)
# 练习4-3：数到20 使用一个for 循环打印数1～20（含）。
for i in range(21):
    print(i)
"""
练习4-4：一百万 创建一个包含数1～1 000 000的列表，再使
用一个for 循环将这些数打印出来。（如果输出的时间太长，
按Ctrl + C停止输出或关闭输出窗口。
"""
# list_number = list(range(1,1000001))
# for i in list_number:
#     print(i)
"""
练习4-5：一百万求和 创建一个包含数1～1 000 000的列
表，再使用min() 和max() 核实该列表确实是从1开始、到1
000 000结束的。另外，对这个列表调用函数sum() ，看看
Python将一百万个数相加需要多长时间
"""
list_number = list(range(1, 1000001))
print(min(list_number))
print(max(list_number))
print(type(list_number))
print(sum(list_number))

sum_list_number = 0
for number in list_number:
    sum_list_number += number
print(sum_list_number)

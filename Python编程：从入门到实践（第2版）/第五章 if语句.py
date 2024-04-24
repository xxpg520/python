# """练习5-1：条件测试
# 编写一系列条件测试，将每个测试以及对其结果的预测和实际结果打印出来。你编写的代码应类似于下面这样：
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi'
# """
# car = 'bmw'
# if car == 'bmw':
#     print('is car == "bmw"? i predict True.')
#
# if car == 'audi':
#     print('is car == "audi"? i predict False.')
# else:
#     print('car == "audi" is False.')
#
# """
# 练习5-3：外星人颜色 假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其赋值为'green'、'yellow' 或'red' 。
# 编写一条if 语句，检查外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了5分。编写这个程序的两个版本，在一个版本中上述测试通过
# 了，而在另一个版本中未通过（未通过测试时没有输出）。
# """
# alien_color = str(input("请输入：'green'、'yellow' 或'red'："))
# if alien_color == 'green':
#     print("你获得了5分")
#
#
# """
# 练习5-4：外星人颜色2 像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5分
# 。如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分。编写这个程序的两个版本，在一个版本中执行if 代码块，在另一个版本中执行else 代码块
# """
# alien_color = str(input("请输入：'green'、'yellow' 或'red'："))
# if alien_color == 'green':
#     print('你获得了5分')
# else:
#     print("你获得了10分")
#
# """
# 练习5-5：外星人颜色3 将练习5-4中的if-else 结构改为if-elif-else 结构。如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。如果外星人是黄色
# 的，就打印一条消息，指出玩家获得了10分。如果外星人是红色的，就打印一条消息，指出玩家获得了15分。编写这个程序的三个版本，分别在外星人为绿色、黄色和
# 红色时打印一条消息。
# """
# alien_color = str(input("请输入：'green'、'yellow' 或'red'：\n"))
# if alien_color == 'green':
#     print('你获得了5分')
# elif alien_color == 'yellow':
#     print("你获得了10分")
# elif alien_color == 'red':
#     print("你获得了15分")
# else:
#     print("请根据提示输入")
#
# """
# 练习5-6：人生的不同阶段 设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断一个人处于人生的哪个阶段。
# 如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
# 如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。
# 如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。
# 如果年龄为13（含）～20岁，就打印一条消息，指出这个人是青少年。
# 如果年龄为20（含）～65岁，就打印一条消息，指出这个人是成年人。
# 如果年龄超过65岁（含），就打印一条消息，指出这个人是老年人。
# """
# age = int(input("请输入你当前年龄（1~100）：\n"))
# if age <2:
#     print("这是一个婴儿")
# elif 2 <= age < 4:
#     print("这是一个幼儿")
# elif 4 <= age < 13:
#     print("这是一个儿童")
# elif 13 <= age < 20:
#     print("这是一个青少年")
# elif 20 <= age < 65:
#     print("这是一个成年人")
# else:
#     print("这是一个老年人")
#
# """
# 练习5-7：喜欢的水果
# 创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句，检查列表中是否包含特定的水果。
# 将该列表命名为favorite_fruits ，并在其中包含三种水果。
# 编写5条if 语句，每条都检查某种水果是否包含在列表中。如果是，就打印一条消息，下面是一个例子。
# You really like bananas!
# """
# favorite_fruits = ['apple', 'banana', 'orange']
# if 'apple' in favorite_fruits:
#     print("You really like apple!")
# if 'banana' in favorite_fruits:
#     print("You really like banana!")
# if 'orange' in favorite_fruits:
#     print("You really like orange!")
# if 'mango' in favorite_fruits:
#     print("You really like mango!")
# if 'grape' in favorite_fruits:
#     print("You really like grape!")
#
# """
# 练习5-8：以特殊方式跟管理员打招呼
# 创建一个至少包含5个用户名的列表，且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条
# 问候消息。遍历用户名列表，并向每位用户打印一条问候消息。如果用户名为'admin' ，就打印一条特殊的问候消息，如下所示。
# Hello admin, would you like to see a status report?
# 否则，打印一条普通的问候消息，如下所示。
# Hello Jaden, thank you for logging in again.
# """
# user = ['acer', 'apple', 'xiaomi', 'huawei','admin']
# for user in user:
#     if user == 'admin':
#         print(f"Hello {user}, would you like to see a status report?")
#     else:
#         print(f"Hello {user}, thank you for logging in again.")
#
# """
# 练习5-9：处理没有用户的情形 在为完成练习5-8编写的程序中，添加一条if 语句，检查用户名列表是否为空。如果为空，就打印如下消息。
# We need to find some users!
# 删除列表中的所有用户名，确定将打印正确的消息。
# """
# user = ['acer', 'apple', 'xiaomi', 'huawei','admin']
# # user = []
# if user:
#     for user in user:
#         if user == 'admin':
#             print(f"Hello {user}, would you like to see a status report?")
#         else:
#             print(f"Hello {user}, thank you for logging in again.")
#
# """
# 练习5-10：检查用户名
# 按下面的说明编写一个程序，模拟网站如何确保每位用户的用户名都独一无二。创建一个至少包含5个用户名的列表，并将其命名为current_users 。再创建一个
# 包含5个用户名的列表，将其命名为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。遍历列表new_users ，对于其中的每个用户名，
# 都检查它是否已被使用。
# 如果是，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
# 确保比较时不区分大小写。换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN' 。
# （为此，需要创建列表current_users 的副本，其中包含当前所有用户名的小写版本。）
# """
# current_users = ['ACER', 'APPLE', 'XiaoMi', 'Huawei', 'AMD']
# new_users = ['philips', 'samsung', 'huawei', 'xiaomi', 'inter']
# new_current_users = [x.lower() for x in current_users]
# for new_users in new_users:
#     if new_users in new_current_users:
#         print(f"用户名：{new_users}已经被使用")
#     else:
#         print(f"用户名：{new_users}未被使用")
#
# """
# 练习5-11：序数
# 序数表示位置，如1st和2nd。序数大多以th结尾，只有1、2和3例外。在一个列表中存储数字1～9。遍历这个列表。
# 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容应为"1st 2nd 3rd 4th 5th 6th 7th 8th 9th" ，但每个序数都独占一行。
# """
# numbers = list(range(1,10))
# for number in numbers:
#     if number == 1:
#         print(f"{number}st")
#     elif number == 2:
#         print(f"{number}nd")
#     elif number == 3:
#         print(f"{number}rd")
#     else:
#         print(f"{number}th")
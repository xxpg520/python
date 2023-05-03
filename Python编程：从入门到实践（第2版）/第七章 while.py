# """
# 练习7-4：比萨配料
# 编写一个循环，提示用户输入一系列比萨配料，并在用户输入'quit' 时结束循环。
# 每当用户输入一种配料后，都打印一条消息，指出我们会在比萨中添加这种配料。
# """
# active = True
# pizaas = []
# while active:
#     配料 = input("请输入你想要的配料：")
#     if 配料 == 'quit':
#         active = False
#     else:
#         pizaas.append(配料)
#         print(f"您要添加的{配料}已经添加到您的披萨中。")
#
# pizaa = '、'.join(pizaas)
# print(f"我们会在比萨中添加：{pizaa}")

"""
练习7-5：电影票
有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3～12岁的观众收费10美元；超过12岁的观众收费15美元。
请编写一个循环，在其中询问用户的年龄，并指出其票价。
"""
active = True
while active:
    age = int(input("请输入您的年龄："))
    if age < 3:
        print(f"您的年龄为：{age},您不足3岁，可免费观影。")
    elif 3 <= age <= 12:
        print(f"您的年龄为：{age},属于少年，可按优惠价10元购票观影。")
    elif age > 12:
        print(f"您的年龄为：{age}，已经成年，应按全价15元购票观影。")
    else:
        print("请输入正确年龄！")


# """
# 练习7-8：熟食店
# 创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字，再创建一个名为finished_sandwiches 的空列表。
# 遍历列表sandwich_orders ，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich ，并将其移到列表finished_sandwiches 中。
# 所有三明治都制作好后，打印一条消息，将这些三明治列出来。
# """
# sandwich_orders = ['水果三明治', '肉松三明治', '蔬菜沙拉三明治']
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(sandwich)
#     print(f"I made your tuna {sandwich}")
# print("你的三明治已经做好：")
# for finished_sandwiches in finished_sandwiches:
#     print(finished_sandwiches)
#
# """
# 练习7-9：五香烟熏牛肉卖完了
# 使用为完成练习7-8而创建的列表sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。
# 在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉（pastrami）卖完了；
# 再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。
# 确认最终的列表finished_sandwiches 未包含'pastrami' 。
# """
# sandwich_orders = ['水果三明治', '五香烟熏牛肉', '肉松三明治', '五香烟熏牛肉', '蔬菜沙拉三明治', '五香烟熏牛肉']
# print("熟食店的五香烟熏牛肉（pastrami）卖完了")
# while "五香烟熏牛肉" in sandwich_orders:
#     sandwich_orders.remove("五香烟熏牛肉")
#     print(f"当前只有{sandwich_orders}")
#
# """
# 练习7-10：梦想的度假胜地
# 编写一个程序，调查用户梦想的度假胜地。使用类似于下面的提示，并编写一个打印调查结果的代码块。
# If you could visit one place in the world, where would you go?
# """
# citys = []
# active = True
# while active:
#     city = input("如果您可以访问世界上的一个地方，您会去哪里？")
#     pd = input("你还有想去的地方吗？（是/否)")
#     citys.append(city)
#     if pd == '否':
#         active = False
# print("你想去的地方有：")
# for i in citys:
#     print(i)
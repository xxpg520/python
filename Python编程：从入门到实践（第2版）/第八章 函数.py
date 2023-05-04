# """
# 练习8-1：消息
# 编写一个名为display_message() 的函数，它打印一个句子，指出你在本章学的是什么。
# 调用这个函数，确认显示的消息正确无误
# """
# def display_message():
#     print("本章内容为函数")

# display_message()

# """
# 练习8-2：喜欢的图书 
# 编写一个名为favorite_book() 的函数，其中包含一个名为title 的形参。这个函数打印一条消息，下面是一个例子。
# One of my favorite books is Alice in Wonderland.
# 调用这个函数，并将一本图书的名称作为实参传递给它。
# """
# def favorite_book(title):
#     print(f"我最喜欢的一般书是《{title}》.")

# favorite_book("战争与和平")
#
# """
# 练习8-3：T恤
# 编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
# 使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。
# """
# def make_shirt(size, font_style):
#     print(f"您要的衬衫尺寸为：{size}号，上面要印的内容：{font_style}。")
#
# make_shirt('s', '学python')
#
# """
# 练习8-4：大号T恤
# 修改函数make_shirt() ，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。
# 调用这个函数来制作：一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）。
# """
# def make_shirt(size = '大号', font_style = 'I love Python'):
#     print(f"您要的T恤尺寸为：{size}，" + f"上面印有：{font_style}")
# make_shirt()
# make_shirt('中号')
# make_shirt('小号', 'I love c++')
#
# """
# 练习8-5：城市
# 编写一个名为describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，下面是一个例子。
# Reykjavik is in Iceland.
# 给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
# """
# def describe_city(city = 'yunnan', country = 'china'):
#     print(f"{city.title()} is in {country.title()}")
#
# describe_city()
# describe_city('kunming', 'china')
# describe_city('tokyo', 'japan')
# describe_city('new york', 'america')
#
# """
# 练习8-6：城市名
# 编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面的字符串：
# "Santiago, Chile"
# 至少使用三个城市国家对来调用这个函数，并打印它返回的值。
# """
# def city_country(city, country):
#      f"{city}, {country}"
#     return f"{city}.title(), {country}.title()"
#
# city_country_1 = city_country('santiago', 'chile')
# city_country_2 = city_country('new york', 'america')
# city_country_3 = city_country('tokyo', 'japan')
#
# print(city_country_1)
# print(city_country_2)
# print(city_country_3)
#
# """
# 练习8-7：专辑
# 编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
#     给函数make_album() 添加一个默认值为None 的可选形参，以便存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，
#     就将该值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数.
# """
# def make_album(singer, album, music_number=None):
#     dict_album = {"singer": singer,"album": album}
#     if music_number is not None:
#         dict_album["music_number"] = music_number
#     return dict_album
# album1 = make_album('周杰伦', '七里香')
# album2 = make_album('林俊杰', '江南', 3)
# album3 = make_album('张韶涵', '你的微笑', 7)
#
# print(album1,album2,album3)
# print(album2['singer'])
# print(album3['music_number'])
# #
# #
# """
# 练习8-8：用户的专辑
# 在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入专辑的歌手和名称。获取这些信息后，
# 使用它们来调用函数make_album() 并将创建的字典打印出来。在这个while 循环中，务必提供退出途径。
# """
# while True:
#     singer = input("请输入歌手名字：")
#     if singer == 'q':
#         break
#     album = input("请输入歌手专辑：")
#     if album == 'q':
#         break
#     print(make_album(singer, album)
# )
#
# """
# 练习8-9：消息
# 创建一个列表，其中包含一系列简短的文本消息。将该列表传递给一个名为show_messages() 的函数，这个函数会打印列表中的每条文本消息。
# """
# """定义函数，将收到的列表打印，返回列表"""
# def show_messages(message):
#     for message in message:
#         print(f"show_messages函数:{message}")
# """创建列表"""
# list1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']
# """调用函数，将列表传参"""
# show_messages(list1)
# """
# 练习8-10：发送消息
# 在你为完成练习8-9而编写的程序中，编写一个名为send_messages() 的函数，将每条消息都打印出来并移到一个名为sent_messages 的列表中。
# 调用函数send_messages() ，再将两个列表都打印出来，确认正确地移动了消息。
# """
# # 定义函数，将得到的列表内容打印
# def show_messages(message):
#     for message in message:
#         print(f"show_messages函数:{message}")
#
# # 定义函数，用来将 列表1 的内容移动到 列表2
# def send_messages(列表1, 列表2):
#     while 列表1:
#         """移动列表1 下标为0的元素到message变量中"""
#         message = 列表1.pop(0)        # pop(0)表示正序移动，第二次循环因为0号元素已经移走，原先的1号元素则成为0号元素
#         print(f"移动:{message} 到列表2")     # 提示移动
#         列表2.append(message)         # 将变量message中的元素添加到列表2中
#
# # 创建2个列表，list1有内容，list2无内容
# list1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']
# list2 = []
#
# # 调用函数
# show_messages(list1)            # 将list1内容打印
# send_messages(list1, list2)     # 将list1内容移动到list2
#
# print(list1)
# print(list2)
#
# """
# 练习8-11：消息归档
# 修改你为完成练习8-10而编写的程序，在调用函数send_messages() 时，向它传递消息列表的副本。
# 调用函数send_messages() 后，将两个列表都打印出来，确认保留了原始列表中的消息。
# """
# # 定义函数，将得到的列表内容打印
# def show_messages(message):
#     for message in message:
#         print(f"show_messages 函数:{message}")
#
# # 定义函数，用来将 list_one 的内容移动到 list_two
# def send_messages(list_one, list_two):
#     while list_one:
#         """移动列表1 下标为0的元素到message变量中"""
#         message = list_one.pop()                # pop(0)表示正序移动，第二次循环因为0号元素已经移走，原先的1号元素则成为0号元素
#         print(f"移动:{message} 到 列表2")      # 提示移动
#         list_two.append(message)                 # 将变量message中的元素添加到列表2中
#     print(list_one)
#     print(list_two)
# # 创建2个列表，list1有内容，list2无内容
# list1 = ['one', 'two', 'three',]
# list2 = []
# # 调用函数
# show_messages(list1)
# send_messages(list1, list2)
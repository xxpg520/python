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

"""
练习8-6：城市名
编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面的字符串：
"Santiago, Chile"
至少使用三个城市国家对来调用这个函数，并打印它返回的值。
"""

"""
练习8-7：专辑 
编写一个名为make_album() 的函数，它创建一个᧿述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
    给函数make_album() 添加一个默认值为None 的可选形参，以便存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，
    就将该值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数.
"""

"""
练习8-8：用户的专辑 
在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入专辑的歌手和名称。获取这些信息后，
使用它们来调用函数make_album() 并将创建的字典打印出来。在这个while 循环中，务必提供退出途径。
"""
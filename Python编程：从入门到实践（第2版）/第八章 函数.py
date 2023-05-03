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
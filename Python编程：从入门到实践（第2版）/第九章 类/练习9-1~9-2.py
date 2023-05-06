"""
练习9-1：餐馆 创建一个名为Restaurant 的类，为其方法__init__() 设置属性restaurant_name 和cuisine_type 。
创建一个名为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法
"""
class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"\n我开了一家名叫{self.restaurant_name}的餐厅，")
		print(f"是一家{self.cuisine_type}风味的餐厅。")

	def open_restaurant(self):
		print(f"餐厅正在营业")

restaurant = Restaurant('胖子', '法式')
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""
练习9-2：三家餐馆 根据为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
"""
my_restaurant = Restaurant('娟娟', '四川')
my_restaurant.describe_restaurant()

restaurant2 = Restaurant('荣记', '港式')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('一味', '日式')
restaurant3.describe_restaurant()
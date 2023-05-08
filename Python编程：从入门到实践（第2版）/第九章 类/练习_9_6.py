"""
练习9-6：冰激凌小店
冰激凌小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承为完成练习9-1或练习9-4而编写的Restaurant 类。
这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。
添加一个名为flavors 的属性，用于存储一个由各种口味的冰激凌组成的列表。
编写一个显示这些冰激凌的方法。创建一个IceCreamStand 实例，并调用这个方法。
"""
class Restaurant:
	"""创建一个类"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化成员变量 餐厅名称 风味"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""输出餐厅描述信息"""
		print(f"\n我开了一家名叫{self.restaurant_name}的餐厅，")
		print(f"是一家{self.cuisine_type}风味的餐厅。")

	def open_restaurant(self):
		"""提示餐厅正在营业"""
		print(f"餐厅正在营业")

class IceCreamStand(Restaurant):
	"""模拟一个冰淇淋摊位。"""

	def __init__(self, restaurant_name, cuisine_type):
		"""初始化父类属性"""

		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def icecream_flavors(self):
		print(f"冰淇淋口味有：")
		for self.flavors in self.flavors:
			print(f"-{self.flavors}")
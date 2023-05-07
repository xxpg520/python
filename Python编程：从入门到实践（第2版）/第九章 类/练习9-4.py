"""
练习9-4：就餐人数
在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实例。
打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
添加一个名为set_number_served() 的方法，让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
添加一个名为increment_number_served() 的方法，让你能够将就餐人数递增。
调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
"""

"""创建一个餐厅类"""
class Restaurant:
	"""定义类中的成员变量"""
	# restaurant_name 餐厅名字
	# cuisine_type    餐厅风格
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""描述餐厅 输出餐厅名、餐厅风格、就餐人数"""
		print(f"\n我开了一家名叫{self.restaurant_name}的餐厅，")
		print(f"是一家{self.cuisine_type}风味的餐厅。")
		print(f"已经有{self.number_served}位顾客来这里就餐。")

	def open_restaurant(self):
		"""输出餐厅当前状态营业"""
		print(f"餐厅正在营业")

	def set_number_served(self,number_served):
		if number_served >= self.number_served:
			self.number_served = number_served
		else:
			print(f"请录入正确的顾客就餐人数。")

	def increment_number_served(self, number):
		self.number_served += number

restaurant = Restaurant('红嫂', '家常菜')
restaurant.set_number_served(5)
restaurant.describe_restaurant()
star = True
while star:
	star = input("请输入今天的顾客人数：")
	if star == 'q':
		star = False
	else:
		restaurant.increment_number_served(int(star))
		restaurant.describe_restaurant()
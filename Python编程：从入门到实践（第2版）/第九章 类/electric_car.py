from car import Car

class Battery:
	"""一次模拟电动汽车电瓶的简单尝试。"""

	def __init__(self, battery_size=75):
		"""初始化电瓶的属性。"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息。"""
		print(f"This car has a {self.battery_size}-kwh battery")

	def get_range(self):
		"""打印一条描述电瓶的续航里程的消息。"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about:{range} miles on a full charge")

class ElectricCar(Car):
	"""电动汽车的独特指出。"""

	def __init__(self, make, model, year):
		"""
		初始化父类属性。
		再初始化电动汽车特有的属性。
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

my_car = ElectricCar('bmw', '750', 2015)
print(f"{my_car.get_descriptive_name()}")
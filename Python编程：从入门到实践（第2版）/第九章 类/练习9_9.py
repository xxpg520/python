"""
练习9-9：电瓶升级
在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。
该方法检查电瓶容量，如果不是100，就将其设置为100。
创建一辆电瓶容量为默认值的电动汽车，调用方法get_range() ，然后对电瓶进行升级，并再次调用get_range() 。
你将看到这辆汽车的续航里程增加了。
"""
class Car:
	"""一次模拟汽车的简单尝试。"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles


class Battery:
	"""一次模拟电动汽车点评的简单尝试。"""

	def __init__(self, battery_size=75):
		"""初始化电瓶的属性。"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息。"""
		print(f"This car has a {self.battery_size}-kwh battery")

	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程。"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about:{range} miles on a full charge")

	def upgrade_battery(self):
		"""重置电瓶容量"""
		if self.battery_size != 100:
			self.battery_size = 100
			print(f"\nBattery capacity reset to {self.battery_size}%")

class ElectricCar(Car):
	"""电动汽车的独特指出。"""

	def __init__(self, make, model, year):
		"""
		初始化父类属性。
		再初始化电动汽车特有的属性。
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

"""创建一个电动车实例，打印相关信息"""
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

"""查询电瓶车容量和剩余里程"""
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

"""调用battery中重置容量的成员方法，再次查询电瓶车容量和剩余里程"""
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
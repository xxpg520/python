class Dog:
	"""一次模拟小狗的简单尝试，"""

	def __init__(self, name, age):
		"""初始化属性name和age，"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗收到命令时蹲下。"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""模拟小狗收到命令时打滚。"""
		print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
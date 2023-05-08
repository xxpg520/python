"""
练习9-3：用户
创建一个名为User的类，其中包含属性first_name 和last_name ，以及用户简介通常会存储的其他几个属性。
在类User 中定义一个名为describe_user() 的方法，用于打印用户信息摘要。再定义一个名为greet_user() 的方法，用于向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例调用上述两个方法
"""
class User:
	def __init__(self, first_name, last_name, user_name, email, location):
		self.first_name = first_name
		self.last_name = last_name
		self.user_name = user_name
		self.email = email
		self.location = location

	def desoribe_user(self):
		print(f"\n{self.first_name}{self.last_name}:")
		print(f"    user_name:{self.user_name}")
		print(f"    email:{self.email}")
		print(f"    location:{self.location}")

	def greet_user(self):
		self.name = f"{self.first_name}{self.last_name}"
		print(f"Welcome black,{self.name}!")

user1 = User('子', '胖', '子胖', 'pangzi@hotmail.com', 'beijing')
user1.desoribe_user()
user1.greet_user()

user2 = User('fei', 'zhang', 'feizhang', 'zhangfei@gmail.com', 'sanguo')
user2.desoribe_user()
user2.greet_user()
"""
练习9-5：尝试登录次数
在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。
编写一个名为increment_login_attempts() 的方法，将属性login_attempts 的值加1。
再编写一个名为reset_login_attempts() 的方法，将属性login_attempts 的值重置为0。
根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。
打印属性login_attempts 的值，确认它被正确地递增。
然后，调用方法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。
"""
class User:
	"""创建User类 定义成员变量"""
	def __init__(self, first_name, last_name, user_name, email, location):
		self.first_name = first_name
		self.last_name = last_name
		self.user_name = user_name
		self.email = email
		self.location = location
		self.login_attempts = 0

	def increment_login_attempts(self):
		"""登录次数+1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""重置登录次数"""
		self.login_attempts = 0

	def desoribe_user(self):
		"""打印用户的信息"""
		print(f"\n{self.first_name}{self.last_name}:")
		print(f"    user_name:{self.user_name}")
		print(f"    email:{self.email}")
		print(f"    location:{self.location}")
		print(f"    login_attempts:{self.login_attempts}")

	def greet_user(self):
		"""将用户名组合并输出欢迎语句"""
		self.name = f"{self.first_name}{self.last_name}"
		print(f"Welcome black,{self.name}!")

# 调用类对象生成实列
user1 = User('fei', 'zhang', 'feizhang', 'zhangfei@gmail.com', 'sanguo')

# 调用成员方法
user1.desoribe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.desoribe_user()
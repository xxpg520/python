"""
练习9-7：管理员
管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承为完成练习9-3或练习9-5而编写的User 类。
添加一个名为privileges 的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"canban user" 等）组成的列表。
编写一个名为show_privileges() 的方法，显示管理员的权限。
创建一个Admin 实例，并调用这个方法。
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


class Admin(User):
	"""描述一个管理员账户。"""

	def __init__(self, first_name, last_name, user_name, email, location):
		"""初始化父类定义"""

		super().__init__(first_name, last_name, user_name, email, location)
		"""调用父类参数"""
		self.privileges = []  # 添加成员变量

	def show_privileges(self):
		print(f"The current account is an administrator.\nYou can perform the following operations:")
		for privileges in self.privileges:
			print(f"\t{privileges}")
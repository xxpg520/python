"""
练习9-8：权限 编写一个名为Privileges 的类，它只有一个属性privileges ，其中存储了练习9-7所述的字符串列表。
将方法show_privileges() 移到这个类中。在Admin 类中，将一个Privileges 实例用作其属性。
创建一个Admin 实例，并使用方法show_privileges() 来显示其权限
"""
from 练习9_7 import User

class Admin(User):
	"""描述一个管理员账户。"""

	def __init__(self, first_name, last_name, user_name, email, location):
		"""初始化父类定义"""

		super().__init__(first_name, last_name, user_name, email, location)
		"""调用父类参数"""
		self.privileges = Privileges()  # 添加成员变量

class Privileges:
	"""定义权限类"""
	def __init__(self, privileges=["an add post", "can delete post", "canban user"]):
		self.privileges = privileges

	def show_privileges(self):
		print(f"\nThe current account is an administrator.\nYou can perform the following operations:")
		for privileges in self.privileges:
			print(f"\t{privileges}")
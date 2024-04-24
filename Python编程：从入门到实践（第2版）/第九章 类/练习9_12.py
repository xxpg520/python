"""
练习9-12：多个模块 将User 类存储在一个模块中，并将Privileges 类和Admin 类存储在另一个模块中。
再创建一个文件，在其中创建一个Admin 实例并对其调用方法show_privileges() ，以确认一切依然能够正确运行。
"""

from 练习9_8 import Admin

user_admin = Admin('备', '刘', '刘备', 'liubei@sanguo.com', 1)
user_admin.desoribe_user()
user_admin.privileges.show_privileges()
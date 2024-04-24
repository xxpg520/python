"""
练习9-11：导入Admin 类 以为完成练习9-8而做的工作为基础。
将User 类、Privileges 类和Admin 类存储在一个模块中，
再创建一个文件，在其中创建一个Admin 实例并对其调用方法show_privileges() ，以确认一切都能正确运行。
"""
from 练习9_8 import Admin

admin = Admin('fei', 'zhang', 'zhangfei', 'zhangfei@gmail.com', 1)
admin.desoribe_user()
admin.privileges.show_privileges()
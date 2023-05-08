"""
练习9-10：导入Restaurant 类 将最新的Restaurant 类存储在一个模块中。
在另一个文件中，导入Restaurant 类，创建一个Restaurant 实例并调用Restaurant 的一个方法，以确认import 语句正确无误。
"""
from 练习_9_6 import Restaurant
my_restaurant = Restaurant('红嫂','家常菜')
my_restaurant.describe_restaurant()
my_restaurant.restaurant_name = '秀玉'
my_restaurant.describe_restaurant()
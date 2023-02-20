"""
演示Python的input语句
获取键盘的输入信息
input()默认接受内容为类型
"""
# name = input("请告诉我你是谁？")
# print("我知道到了，你是：%s" % name)
#
# # 输入数字类型
# num = input("请告诉我你的银行卡密码：")
# # 数据类型转换
# num = int(num)
# print("你的银行卡密码的类型是：", type(num))

"""
练习
定义2个变量，用以获取从键盘输入的内容，并给出提示信息；
· 变量1，变量名：user_name，记录用户名称
· 变量2，变量名：user_type,记录用户类型
"""

user_name = input("请输入您的用户名：")
user_type = "SSSSSVIP"
print(f"您好：{user_name},您是尊贵的：{user_type} 用户，欢迎您的光临")

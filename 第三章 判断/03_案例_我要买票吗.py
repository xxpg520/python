"""
练习案例：我要买票吗
通过input语句获取键盘输入的身高
判断身高是否超过120cm，并通过print给出提示信息

欢迎来到黑马动物园
请输入你的身高（cm）：130
您的身高超出120cm，游玩需要购票10元。
祝您游玩愉快

欢迎来到黑马动物园
请输入您的身高（cm）：111
您的身高未超过120cm，可以免费游玩
祝您游玩愉快
"""
# 定义键盘输入获取身高数据
height = int(input("请输入您的身高（cm）："))

# 通过if进行判断
if height >= 120 :
    print("您的身高超出120cm，游玩需要购票10元。")
else:
    print("您的身高未超过120cm，可以免费游玩。")

print("祝您游玩愉快.")

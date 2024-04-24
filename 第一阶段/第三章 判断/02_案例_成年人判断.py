"""
联系案例：成年人判断
结合前面学习的input输入语句，完成如下案例：
1、通过input语句，获取键盘输入，为变量age赋值。（注意转换成数字类型）
2、通过if判断是否是成年人，满足条件则输出提示信息，如下：
欢迎来到黑马儿童游乐场，儿童免费，成人收费。
请输入你的年龄：30
您已成年，游玩需要补票10元。
祝您游玩愉快
"""
age = int(input("欢迎来到黑马儿童游乐场，儿童免费，成人收费。\n请输入您的年龄："))
if age >= 18:
    print("你已成年，游玩需要补票10元。")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快。")
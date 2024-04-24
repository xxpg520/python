"""
演示判断语句的嵌套使用
"""

# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制，不可以免费")
#     print("但是，如果vip级别大于3，可以免费")
#     if int(input("你的vip界别是多少：")) > 3:
#         print("恭喜你，vip级别达标，可以免费")
#     else:
#         print("Sorry，你需要买票10元")
# else:
#     print("欢迎小朋友，免费游玩")

age = 11
year = 1
level = 1
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标了，可以领取礼物")
        elif level > 3:
            print("恭喜你，你的年龄和级别都达标了，可以领取礼物")
        else:
            print("很遗憾，你的入职时间和级别都不达标，无法领取礼物")
    else:
        print("很遗憾，您的年龄超过30岁，无法领取礼物")
else:
    print("很遗憾，您的年龄不满18岁，无法领取礼物")
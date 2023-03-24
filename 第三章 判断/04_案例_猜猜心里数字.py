"""
1、定义一个变量，数字类型，内容随意。
2、基于input语句输入猜想的数字，通过if和多次elif的组合，判断猜想数字是否和心里数字一直。
"""
num = 5
if int(input("请输入我心里想的数字：")) == num:
    print("恭喜第一次就猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print(f"Sorry,全部猜错啦，我想的是{num}")

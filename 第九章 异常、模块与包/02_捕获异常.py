"""
演示捕获异常
"""
# # 基本捕获语法
#
# try:
#     f = open("d:/abc.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常了,因为文件不存在, 我将open模式改为'w'去打开")
#     f = open("d:/abc.txt", "w", encoding="UTF-8")
#
# # 捕获指定的异常
try:
    print(name)
    # 1/0
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)
#
# # 捕获多个异常
# try:
#     # 1/0
#     print(name)
# except(NameError, ZeroDivisionError) as e:
#     print("出现了变量未定义 或者 除0的异常错误")

# 捕获所有异常
# try:
#     f = open("d:/123.txt", "r", encoding="UTF-8")
#     # print("hello")
# except Exception as e:
#     print(f"出现'{e}'异常了")
#     f = open("d:/123.txt", "w", encoding="UTF-8")
# else:
#     print("很高兴,没有异常")
# finally:
#     print("我是finally, 有没有异常我都会执行")
#     f.close()
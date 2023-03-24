# 规则1: 内容限定，限定只能使用：中文/英文/数字/下划线
#  错误的代码示范：1_name = "张三"
#  错误胡代码示范:  name_! = "张三"
name_ = "张三"
_name = "张三"
name_ = "张三"

# 规则2: 大小写敏感
Itheima = "黑马程序员"
itheima = 666
print(Itheima)
print(itheima)

# 规则3: 不可以使用关键字
# 错误的示例, 使用了关键字 class = 1
# 错误的示例, 使用了关键字 def = 1
Class = 1

"""
演示面向对象类中的成员方法定义和使用
"""

# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好啊,我是{self.name},欢迎大家多多关照")

stu = Student()
stu.name = "周杰轮"
stu.say_hi()

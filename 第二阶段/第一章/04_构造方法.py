"""
演示类的构造方法
"""
# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称：__init__

class Student:
    name = None
    age = None
    tel = None
    # 在构造方法内定义成员变量，需要使用self关键字
    def __init__(self, name, age, tel):
        self.name = name        # 姓名
        self.age = age          # 年龄
        self.tel = tel          # 电话
        print("Student类创建了一个类对象")
stu = Student("周杰伦", 31, "18500006666")
print(stu.name)
print(stu.age)
print(stu.tel)

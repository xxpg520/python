"""
演示Python内置的各类魔术方法
"""

class Student:

    # __init__ 构造方法，可用于创建类对象的时候设置初始化行为
    def __init__(self, name, age):
        self.name = name        # 学生姓名
        self.age = age          # 学生年龄

    # __str__ 魔术方法 用于实现对象转字符串的行为
    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

    # __lt__魔术方法 用于2个类对象进行小于或大于比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法 用于2个类对象进行小于等于或大于等于比较
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法 用于2个类对象进行相等比较
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("周杰轮", 36)
stu2 = Student("林俊节", 36)
print(stu1 == stu2)





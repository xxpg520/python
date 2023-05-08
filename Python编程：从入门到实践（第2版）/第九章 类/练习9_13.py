"""
练习9-13：骰子
创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。
编写一个名为roll_die() 的方法，它打印位于1和骰子面数之间的随机数。
创建一个6面的骰子再掷10次。
创建一个10面的骰子和一个20面的骰子，再分别掷10次。
"""
from random import randint

class Die:
    """模拟一个骰子"""

    def __init__(self, sides=6):
        """初始化骰子"""
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# 创建一个 6 面的骰子，再掷 10 次并显示结果。
d6 = Die()
rolls = []
for roll_num in range(10):
    rolls.append(d6.roll_die())
print(rolls)

# 创建一个 10 面的骰子，再掷 10 次并显示结果。
d10 = Die(10)
rolls = []
for roll_num in range(10):
    rolls.append(d10.roll_die())
print(rolls)

# 创建一个 10 面的骰子，再掷 10 次并显示结果。
d20 = Die(20)
rolls = []
for roll_num in range(10):
    rolls.append(d20.roll_die())
print(rolls)
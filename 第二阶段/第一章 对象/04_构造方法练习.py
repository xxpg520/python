class Sturdent:
    def __init__(self, name, age, address):
        self.name = name
        self.age =age
        self.address =address
        print(f"学生姓名:{self.name}，年龄:{self.age}，地址:{self.address}")

for sum in range(0,10):
    print(f"当前输入第{sum+1}位学生信息，总共需录入10位学生信息")
    stu = Sturdent(input("请输入学生姓名:"),
               int(input("请输入学生年龄:")),
               input("请输入学生地址:"), )

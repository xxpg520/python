"""
元组的练习案例
定义一个元组，内容是"周杰伦", "11", ["football", "music"]，记录的是一个学生的姓名、年龄、爱好
通过元组的功能（方法），对其进行：
1、查询其年龄所在的下标
2、查询学生的姓名
3、删除学生爱好中的football
4、增加爱好：coding到list内
"""
# 定义一个元组
t1 = ("周杰伦", 11, ["football", "music"])
# 查询其年龄所在的下标
index = t1.index(11)
print(f"年龄的下表是：{index}")

# 查询学生的姓名
print(f"学生的姓名是：{t1[0]}")

# 删除学生爱好中的football
del t1[2][0]
print(t1)

# 增加爱好：coding到list内
t1[2].insert(0, "coding")
print(t1)
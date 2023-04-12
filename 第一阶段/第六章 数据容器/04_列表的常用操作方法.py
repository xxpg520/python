"""
演示数据容器之：list列表的常用操作
"""
mylist = ["itcast", "itheima", "python"]
# 1.1 查找某元素在列表内的下表索引--index(元素)
index = mylist.index("itheima")
print(f"itheima在列表中的下表索引值是：{index}")
# 1.2 如果被查找的元素不存在，会报错
# index = mylist.index("hello")
# print(f"hello在列表中的下表索引值是：{index}")

# 2. 修改特定下表索引值--列表[下标] = 修改值
mylist[0] = "传智教育"
print(f"列表被修改元素值后，结果是：{mylist}")

# 3. 在指定下表位置插入新元素--列表.insert(下标, 元素)
mylist.insert(1, "best")
print(f"列表插入元素后，结果是：{mylist}")

# 4. 在列表的尾部追加'''单个'''新元素 append()
mylist.append("黑马程序员")
print(f"列表在追加了元素后，结果是：{mylist}")

# 5. 在列表的尾部追加'''一批'''新元素 extend()
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"在列表追加一批元素后，结果是：{mylist}")

# 6. 删除指定下标索引的元素 （2种方式）
mylist = ["itcast", "itheima", "python"]

# 6.1 仅删除列表中元素--方式1： del 列表[下标]
del mylist[2]
print(f"列表删除元素后的结果是：{mylist}")

# 6.2 删除列表中元素并将该元素返回--方式2：列表.pop(下标）  需要变量接收返回值
mylist = ["itcast", "itheima", "python"]
element = mylist.pop(2)
print(f"通过pop方法取出元素后列表内容：{mylist}, 取出的元素是：{element}")

# 7. 删除某元素在列表中的 第一个 匹配项  列表.remove(元素)
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
mylist.remove("itheima")
print(f"通过remove方法移除元素后，列表的结果是：{mylist}")

# 8. 清空列表--列表.clear()
mylist.clear()
print(f"列表被清空了，结果是{mylist}")

# 9. 统计列表内某元素的数量  列表.count(元素)  需要变量接收返回值
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
count = mylist.count("itheima")
print(f"列表中itheima的数量是：{count}")

# 10. 统计列表中全部的元素数量  len(列表)
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
count = len(mylist)
print(f"列表的元素数量总共有：{count}")

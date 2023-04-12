"""
演示对文件的读取
"""

# 打开文件
f = open("d:/测试.txt", 'r', encoding="UTF-8")
print(type(f))
# 读取文本 read()方法
# print(f"读取10个字节的结果:{f.read(10)}")
# print(f"read方法读取全部内容的结果是:{f.read()}") # 下一个read会从上一个read后读取
print("------------------------------------")

# 读取文件 - readlines()
# lines = f.readlines() # 读取文件的全部行,封装到列表中
# print(f"lines的对象的类型: {type(lines)}")
# print(f"lines对下的结果是: {lines}")

# 读取文件 -readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是: {line1}")
# print(f"第二行数据是: {line2}")
# print(f"第三行数据是: {line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行数据时: {line}")

# close() 关闭文件对象
# f.close()

# with open 语法操作文件
with open("d:/测试.txt", 'r', encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据时:{line}")

"""
演示读取文件, 课后练习题
"""

# 打开文件 以读取模式打开
f = open("d:/word.txt", "r", encoding="UTF-8")
# 方式1: 读取全部内容, 通过字符串count方法统计itheima单词数量
# content = f.read()  # 读取所有文件存到content变量
# count = content.count("itheima") # 用count函数进行统计
# print(f"itheima在文件中出现了: {count}次")

# 方式2: 读取内容,一行一行读取
count = 0   # 使用count变量来累计itheima出现的次数
for line in f:
    line = line.strip() # 去除开头和借位的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1
print(f"itheima出现的次数是: {count}次")
# 关闭文件
f.close()

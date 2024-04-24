"""
需求分析:
1. 读取文件
2. 将文件写出到bill.txt.bak文件作为北方
3. 同时,将文件内标记为测试的数据行丢弃

实现思路:
1. open和r模式打开一个文件对象,并读取文件
2. open和w模式打开另一个文件对象,用于文件写出
3. for循环内容,判断是否是测试不是测试就write写出,是测试就continue跳过
4. 将2个文件对象菌close()
"""
fr = open("c:/Users/xxpg/Desktop/bill.txt", "r", encoding="UTF-8")
fw = open("c:/Users/xxpg/Desktop/bill.txt.bak", "w", encoding="UTF-8")
for line in fr:
    line = line.strip() # 去掉换行符
    # 判断内容,将满足的内容写出
    if line.split(",")[4] == "测试":     # 用split将line内容以","号分割成一个列表,然后用下标4的列表内容对比"测试"
        continue        # continue 跳过本次循环,本次循环后面内容跳过
    # 将内容写出fw
    fw.write(line)
    # 由于前面进行了strip()操作, 所以要手动写出换行符
    fw.write("\n")
# close 关闭2个对象
fr.close()
fw.close()



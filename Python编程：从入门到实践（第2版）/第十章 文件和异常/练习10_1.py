"""
练习10-1：Python学习笔记
在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，其中每一行都以“In Python you can”打头。
将这个文件命名为learning_python.txt，并存储到为完成本章练习而编写的程序所在的目录中。
编写一个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；
第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with 代码块外打印它们
"""
filename = 'learning_python.txt'

# 第一次打印时读取整个文件
print("--------分割线---------")
with open(filename) as file:
    contents = file.read()
print(contents)

# 第二次打印时遍历文件对象
print("-------分割线----------")
with open(filename) as file:
    for line in file:
        print(line.rstrip())

# 第三次打印时将各行存储在一个列表中，再在with 代码块外打印它们
print("-------分割线----------")
with open(filename) as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())
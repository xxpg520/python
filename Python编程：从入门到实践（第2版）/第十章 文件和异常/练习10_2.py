"""
练习10-2：C语言学习笔记
可使用方法replace() 将字符串中的特定单词都替换为另一个单词。
读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，比如C。
将修改后的各行都打印到屏幕上
"""
# 将路径和文件名存入变量
filename = 'learning_python.txt'

# 打开文件并命名为f
with open(filename) as f:
    """逐行读取并存入列表file"""
    file = f.readlines()

# 遍历列表
for line in file:
    """删除换行符"""
    line = line.rstrip()
    """使用replace()函数进行内容替换保存到ff字符串变量"""
    ff = line.replace("Python", "C")
    print(ff)
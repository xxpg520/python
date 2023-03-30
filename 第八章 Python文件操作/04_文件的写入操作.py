"""
演示文件的写入操作
参数 w 模式
1. 文件不存在则会创建
2. 文件存在则会清空原有内容
"""
import time

# # 打开文件,不存在的文件  r w a
# f = open("c:/Users/xxpg/Desktop/test.txt", "w", encoding="UTF-8")
# # write 写入
# f.write("hello word!!!")    # 将内容写入到内存中
# # flush 刷新
# f.flush()   # 将内存中积攒的内容,写入到硬盘的文件中
# # close 关闭
# f.close()   # close方法, 内置了flush功能

# 打开一个存在的文件
f = open("c:/Users/xxpg/Desktop/test.txt", "w", encoding="UTF-8")
# 用write写入,flush刷新
f.write("黑马程序员")
f.flush()
# close关闭
f.close()


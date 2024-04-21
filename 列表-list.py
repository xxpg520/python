"""
list 列表的使用
"""

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# 用len()查看列表内的元素个数
print(len(classmates))

# 使用索引访问list指定位置的元素,从0开始
# 正序
print(classmates[1])
# 倒序
print(classmates[-1])

# 把元素插入到指定位置insert(序号,'内容')
classmates.insert(1, 'jack')
print(classmates)

# 删除指定位置的元素pop(序号)
classmates.pop(1)
print(classmates)

# 把某个元素替换成别的元素，可以直接复制给对应索引位置
classmates[1] = 'Sarah'
print(classmates)

# list元素也可以是另一个list，比如
s = ['python', 'java',['asp','php'],'scheme']
print(s)
print(len(s))

# 另一种理解
p = ['asp', 'php']
s = ['python', 'java', p,'scheme']
print(s)
print(len(s))


"""
dict字典，使用键-值（key-value）存储
"""

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d["Michael"])
print(d["Bob"])
print(d["Tracy"])


# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print("Michael" in d)
# 返回True或者False

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，
print(d.get('Thomas'))
# 或者自己指定的value：
print(d.get('Thomas', -1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop("Bob"))
print(d)


"""
set集合
"""
s = {1, 2, 2, 3, 3}
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)

# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # 可以比较s1和s2中都有的内容并输出
print(s1 | s2)  # 把s1和s2中内容列出，不展示重复内容


a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
x = a.replace('a', 'A')
print(x)
print(a)
"""
演示字符串大小比较
1. 字符串如何比较
    从头到尾,一位位进行比较,其中一位打,后面就无需比较了.
2. 单个字符质检如何确定大小?
    通过ASCII码表, 确定字符对应的码值数字来确定大小
"""

# abc 比较 abd
print(f"abd大于abc, 结果:{'abd' > 'abc'}")

# a 比较 ab
print(f"ab大于a, 结果: {'ab' > 'a'}")

# a 比较 A
print(f"a 大于 A, 结果: {'a' > 'A'}")

# key1 比较 key2
print(f"key2 > key1, 结果:{'key2' > 'key1'}")
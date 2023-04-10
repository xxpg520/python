"""
演示第三个图标：GDP动态柱状图开发
"""
from pandas.core.internals.construction import dataclasses_to_dicts

# 读取数据
f = open("D:/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典存储，格式为：
# { 年份:[[国家, gdp],[国家，gdp],…………]，年份:[[国家,gdp],[国家，gdp],…………]…………}
# {1960:[[美国, 123],[中国，321],…………]，1961:[[美国,gdp],[中国，321]…………]…………}
# 先定义一个字典对象
data_dict = {}

"""
演示第三个图标：GDP动态柱状图开发
"""

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
for line in data_lines:
    year = int(line.split(",")[0])      # 年份
    country = line.split(",")[1]        # 国家
    gdp = float(line.split(",")[2])     # gdp数据
    # 如何判断字典里面有没有key呢?

    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] =[]
        data_dict[year].append([country, gdp])

# 排序年份
sorted_year_list = data_dict.keys()
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1],reverse=True)
    # 取出本年份前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []

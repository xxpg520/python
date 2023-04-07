"""
演示全国疫情可视化地图开发
"""
import json
# 读取数据文件
f = open("d:/疫情.txt", "r", encoding="UTF-8")
data = f.read()
print(data)
# 关闭文件
f.close()
# 取到各省数据
# 将字符串json转换为Python的字典
data_dict = json.loads(data)        # 基础数据字典
# 从字典中取出省份数据
pro = data_dict["areaTee"][0]["children"]
# 组装每个省份和确诊人数为元组，并并各个省的数据都封装入列表内

# 创建地图对象

# 添加数据

# 设置全局配置，制定分段的视觉映射

# 绘图